---
title: "Migrating and Rewriting the History of a Git Repository"
description: "Some handy notes and things I learned while scrubbing the history a large git repository with lots of history, and migrated it to a new URL."
date: 2025-01-27
tags: [git, git-filter-repo, shell, bash]
---

These are some handy notes and things I learned while scrubbing the history of a large git repository with lots of history, and migrating it to a new URL.

I used [git-filter-repo](https://github.com/newren/git-filter-repo) to perform the history scrubbing. It worked really well, and the tool is also the one officially recommended by git itself ([source](https://github.com/git/git/commit/9df53c5de6e687df9cd7b36e633360178b65a0ef)).

## Table of Contents

- [Order of Operations](#order-of-operations)
- [Some handy dandy scripts I wrote](#some-handy-dandy-scripts-i-wrote)
- [Migrating a changeset after scrubbing](#migrating-a-changeset-after-scrubbing)

## Order of Operations

### 1. Clone a "bare" version of the repo

```shell
git clone --bare <repo_url>
```

This clones the entire `.git` directory which includes all the repo's history and refs, but doesn't "materialize" the code into the file system. I'm not sure if this is required, but it was the method recommended in some places online.

### 2. Duplicate and rename the clone

If, like me, you're scrubbing the repo's history, it can be helpful to retain a "dirty" copy of the git history for later comparison and reference. I duplicated the cloned repo, and named one copy `<repo_name>-dirty.git` and the other `<repo_name>-clean.git`. The "dirty" version will remain unmodified, and the "clean" version is where we'll do our work.

### 3. Run `filter-repo`'s analyze

```shell
git filter-repo --analyze
```

This creates a new `filter-repo` directory, and outputs some debug data that may be useful to you later on.

### 4. (Optional) Delete tags and branches you do not want to transfer

As long as I was mucking about with the repo, I decided to do some cleanup while I was in there. I deleted all tags, and deleted all branches except the default (`main` in our case), and any `release` branches that were being actively worked on.

This had some benefits and drawbacks:

#### Benefits

- A cleaner repo is a nicer repo.

#### Drawbacks

- If it turns out that there are branches removed from the new repository, they will beed to be migrated later from the old repository manually.
	- In normal circumstances, this is not a big deal (see instructions below).
	- In the case where (against recommendations), there is a long-running feature branch that contains _a lot_ of work not yet merged to the trunk, it can become quite a pain to migrate.

See the XXXXXX section below for details on how to migrate a changeset in both the simple and complex examples.

### 5. Run the filter pass

You've made it to the exciting part!

```shell
git filter-repo --invert-paths --path-glob <file_glob>
```

`--invert-paths`
:	This instructs `filter-repo` to _remove_ any file specified. By default, it removes anything _except_ the file specified.

`--path-glob`
:	`filter-repo` includes the ability to specify a full file path instead of a glob, but I had less success with that. For some reason, it didn't consistently remove everything from the history as expected. Using a glob instead worked flawlessly, and adds some flexibility, allowing you to target multiple files in one command.
:
:	For example, let's say I needed to remove any reference to all 3 of these files in the git history:
:	- `SecretFileReader.swift`
:	- `SecretFileReaderWriter.swift`
:	- `SecretFileReaderTests.swift`
:
:	Using the glob `**/**/SecretFileReader*.swift` will hit all three files in one pass.

> [!tip]
> It can be useful to use the `find` command to test a file glob before using it with `filter-repo`. For the example above, the command would be:
>
> ```shell
> find . -path '**/**/SecretFileReader*.swift'
> ```

### 6. Verify the files were filtered as expected

This part was very important in my case, as I was scrubbing some possibly sensitive data from the git history.

```shell
git log --name-status --all | grep <name_of_file>
```

That command will look for any instance of the file specified in the entire git history.

> [!tip]
> Run this command on both the "dirty" and "clean" versions of the repo to verify that the dirty version _does_ find results, and the clean version _does not_.

### 7. Delete the existing remotes from the clean version

```shell
git remote | xargs -n 1 git remote remove
```

### 8. Add the new remote to the clean version

```shell
git remote add origin <new_repo_url>
```

### 9. Push all refs to the new location

```shell
git push --all
```

### 10. Go enjoy a tasty beverage

You just did some _truly gnarly_ git surgery. Go have a beer/coffee/tea/etc. to celebrate.

## Some handy dandy scripts I wrote

As is tradition, I wrote a few scripts to help with this whole process. I'm including them here as reference for others. Remember that these are all pretty bespoke, so they most likely will need changes to fit your needs.

### `compare.sh`

After filtering the git history, `filter-repo` produces a `commit-map` file, listing all the commits hashes in the git history alongside the newly assigned hash for that commit if it was modified.

This script compares the before and after git hashes for each line in the `commit-map` file, and prints out just the lines that have been modified. This was helpful for me to understand what changes `filter-repo` actually made to the git history.

```bash
#!/bin/bash

set -o errexit  # Exit on error
set -o nounset  # Exit on unset variable
set -o pipefail # Exit on pipe failure

if [[ "${TRACE:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi

function main() {
	declare -r commit_map_file="$1"

	declare -i line_number=0
	declare -i total_diffs=0

	while IFS=' ' read -r before after; do
		line_number=$((line_number + 1))

		# Skip the first line becase it just contains the column headers
		if [[ "$line_number" -eq 1 ]]; then
			continue
		fi

		if [[ "$before" != "$after" ]]; then
			total_diffs=$((total_diffs + 1))
			echo "Line ${line_number}: ${before} ${after}"
		fi
	done < "$commit_map_file"

	echo
	echo "${line_number} git hashes analyzed"
	echo "${total_diffs} of them have been modified"
}

trap exit_handler EXIT
function exit_handler() {
	declare -ri exit_code="$?"
	if [[ $exit_code -ne 0 ]]; then
		declare -r script_name="${0##*/}"
		echo -e "\n==> ${script_name} exited with code ${exit_code}"
	fi
}

main "$@"
```

### `delete-most-refs.sh`

This script deletes all remotes, tags, and branches, except those specified in the `protected_branches` array. Useful if you're doing the optional step 4 above.

```bash
#!/bin/bash

set -o errexit  # Exit on error
set -o nounset  # Exit on unset variable
set -o pipefail # Exit on pipe failure

if [[ "${TRACE:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi

# This script deletes all remotes, tags, and branches except for the protected branches
# that are listed in the `protected_branches` array.
#
# Be sure to modify the `protected_branches` variable below to suit your needs.

function main() {
	remove_all_remotes
	delete_all_tags
	delete_all_branches_except_protected
	print_results
}

function remove_all_remotes() {
	echo
	echo "==> Removing all remotes"
	git remote | xargs -n 1 git remote remove
}

function delete_all_tags() {
	echo
	echo "==> Deleting all tags"
	git tag | xargs git tag -d
}

function delete_all_branches_except_protected() {
	declare -ra protected_branches=(
		"main"
	)

	echo
	echo "==> Deleting all branches except protected branches: ${protected_branches[*]}"

	declare -a all_branches
	while IFS= read -r -d '' branch; do
		all_branches+=("$branch")
	done < <(git branch --format="%(refname:short)")
	readonly all_branches

	for branch in "${all_branches[@]}"; do
		for protected_branch in "${protected_branches[@]}"; do
			if [[ "$branch" == "$protected_branch" ]]; then
				echo "==> Skipping protected branch: ${branch}"
				continue 2
			fi
		done

		git branch -D "$branch"
	done
}

function print_results() {
	echo
	echo "==> Results"
	echo
	echo "==> Remotes"
	git remote
	echo
	echo "==> Tags"
	git tag
	echo
	echo "==> Branches"
	git branch
	echo
	echo "==> Done"
}

trap exit_handler EXIT
function exit_handler() {
	declare -ri exit_code="$?"
	declare -r script_name="${0##*/}"
	echo -e "\n==> ${script_name} exited with code ${exit_code}"
}

main "$@"
```

### `print-commits-in-order.sh`

The `commit-map` file created by `filter-repo` does not list commits in any specific order. This script prints out the commits chronologically which can be helpful when verifying things worked as expected.

```bash
#!/bin/bash

set -o errexit  # Exit on error
set -o nounset  # Exit on unset variable
set -o pipefail # Exit on pipe failure

if [[ "${TRACE:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi

# This script prints out the commits in order of when they were made.
# It uses the commit-map file that was created by the `filter-repo` script
# to get the commit hashes and the dates they were made.
#
# Best to pipe the output into a file to be able to easily reference it later.
#
# `$ ./print-commits-in-order.sh <path_to_commit_file> > commits-in-order.txt`

function main() {
	declare -r commit_file="$1"

	declare -a commits
	while IFS= read -r -d '' commit; do
		commits+=("$commit")
	done < <(cat "$commit_file")
	readonly commits

	declare -A commit_dates

	set +o errexit
	for commit in "${commits[@]}"; do
		if [[ -z "${commit}" ]]; then
			continue
		fi
		date="$(git show -s --format=%ci "$commit")"
		commit_dates["$commit"]="$date"
	done
	set -o errexit

	for commit in "${!commit_dates[@]}"; do
		echo "${commit_dates[$commit]} $commit"
	done | sort | while read -r line; do
		commit="${line##* }"
		echo "==> ${commit}"
	done
}

trap cleanup EXIT
function cleanup() {
	declare -ri exit_code="$?"
	declare -r script_name="${0##*/}"
	echo -e "\n==> ${script_name} exited with code ${exit_code}"
}

main "$@"
```

## Migrating a changeset after scrubbing

At a high level, this process consists of 2 steps:

1. Export _just the changes_ from the original repository.
2. Import those changes into the new repository.

It's important that _just the changes_ be migrated. If migrating the actual git commits themselves is attempted, this will cause problems. The git history of the old and new repositories is now different, and it will end up trying to copy over the entire git history from the old repository.

### 1. Export _just the changes_ from the original repository

> [!important]
> Perform these actions in your terminal from the root of the **_original_** repository.

#### 1. Pull the latest changes from main to ensure you're up to date

```shell
git switch <default_branch>

git pull

git switch <branch_name>
```

#### 2. Rebase or merge the current default branch onto your branch

```shell
git rebase <default_branch>
```

#### 3. Resolve any conflicts if necessary

My tools of choice here are [Tower](https://www.git-tower.com) and [Kaleidoscope](https://kaleidoscope.app).

#### 4. Export `.patch` files for the changes

```shell
git format-patch <default_branch>..
```

> [!important]
> The double dots here (`..`) are important. Using triple dots will result in different behavior.

This command will create a `.patch` file for every commit that does not exist on the default branch. Depending on the situation, it may be more useful to create a single `.patch` file that contains all of the commits. To do this, pass the `--stdout` flag, and point it to a file path.

```shell
git format-patch <default_branch>.. --stdout > changeset.patch
```

### 2. Import changes into the new repository

> [!important]
> Perform these actions in your terminal from the root of the **_new_** repository.

#### 1. Create a new branch for your changes

```shell
git switch --create <branch_name>
```

#### 2. Apply the patches

```shell
git apply /path/to/original/repository/*.patch
```

> [!note]
> Using `*.patch` at the end here instructs git to apply all files with the `.patch` extension

If you run into issues, try adding the `--3way` flag to the command to perform a 3-way merge:

```shell
git apply --3way /path/to/original/repository/*.patch
```

#### 3. Inspect

Inspect the changes to the new repository to ensure they were applied as expected.

#### 4. LGTM

Commit, push, and carry on.
