#!/usr/bin/env python3

import os
import pathlib
import shutil
import tempfile
import zipfile

import dotenv
import dropbox

dotenv.load_dotenv()

if "DROPBOX_APP_KEY" not in os.environ:
    print("DROPBOX_APP_KEY is not set")
    exit(1)

if "DROPBOX_APP_SECRET" not in os.environ:
    print("DROPBOX_APP_SECRET is not set")
    exit(1)

if "DROPBOX_REFRESH_TOKEN" not in os.environ:
    print("DROPBOX_REFRESH_TOKEN is not set")
    exit(1)

dbx = dropbox.Dropbox(
    app_key=os.getenv("DROPBOX_APP_KEY"),
    app_secret=os.getenv("DROPBOX_APP_SECRET"),
    oauth2_refresh_token=os.getenv("DROPBOX_REFRESH_TOKEN")
)

project_root = pathlib.Path(__file__).parent.parent.absolute()
src_dir = os.path.join(project_root, "src")

temp_dir = tempfile.TemporaryDirectory()


def delete_directory(dir_name):
    directory_path = os.path.join(src_dir, dir_name)
    if os.path.exists(directory_path):
        print(f"Removing    {directory_path}")
        shutil.rmtree(directory_path)


def download_and_extract(dir_name):
    print(f"Downloading {dir_name}")
    result = dbx.files_download_zip("/" + dir_name)
    download_path = os.path.join(temp_dir.name, dir_name + ".zip")
    with open(download_path, "wb") as f:
        f.write(result[1].content)
    with zipfile.ZipFile(download_path, "r") as zip_ref:
        print(f"Extracting  {dir_name} to {src_dir}/{dir_name}")
        zip_ref.extractall(src_dir)


directory_names = ["_posts", "_drafts", "pages"]
for directory_name in directory_names:
    print()
    delete_directory(directory_name)
    download_and_extract(directory_name)
