alias: 2016/11/11/why-commits-to-forks-on-github-dont-count-toward-contributions.html
published_date: 2016-11-11
tags: technology, software, github
title: Why Commits to Forks on GitHub Don't Apply to Contributions
___

Recently, I noticed that contributions I made to forks on GitHub were not being counted toward the contribution tracker on my profile's page. I was curious to know why, as I felt like those contributions were just as good as any other.

After a little research, I found [this article](https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile/) on GitHub's support site. In it, they say:

> Commits made in a fork will not count toward your contributions. To make them count, you must do one of the following:
>
> - Open a pull request to have your changes merged into the parent repository.
> - To detach the fork and turn it into a standalone repository on GitHub, contact GitHub Support.

So I found that there were ways around this, but I still wasn't sure why. So, I emailed GitHub support to get some more information. Their response:

> Hi Isaac,
>
> Forks are designed as temporary places where you can work before merging your commits into the upstream repository. If commits in forks counted towards your contributions, in that workflow you'd end up with two contributions for each commit. One for the fork, one for the upstream repository.
>
> If a fork becomes a different project from it's upstream repository, and will never have commits merged into the upstream repository, then you can ask GitHub Support to detach the fork and turn it into a standalone repository. This will make the commits count towards your contributions. This is described here:
>
> I hope this explains the situation. Let us know if you have any further questions.
>
> Thanks, Alex

This definitely helped my understanding, and makes total sense. I had been using forks incorrectly — not as temporary places to work before merging code back into the master, but as a permanent place for storing work.

So, thank you to Alex at GitHub for clarifying this. I'll be sure to use forks properly, and have correct expectations from now on.
