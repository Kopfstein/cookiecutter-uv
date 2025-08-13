#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, target))


def move_dir(src: str, target: str) -> None:
    shutil.move(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target))


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to_pypi}}" == "n":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" == "basic":
        move_file("Dockerfile_basic", "Dockerfile")
        remove_file("Dockerfile_huggingface")
        remove_file(os.path.join("{{cookiecutter.project_slug}}", "index.html"))
    elif "{{cookiecutter.dockerfile}}" == "huggingface":
        move_file("Dockerfile_huggingface", "Dockerfile")
        remove_file("Dockerfile_basic")
        remove_file(os.path.join("{{cookiecutter.project_slug}}", "__init__.py"))
        remove_file(os.path.join("{{cookiecutter.project_slug}}", "foo.py"))
    elif "{{cookiecutter.dockerfile}}" == "none":
        remove_file("Dockerfile_basic")
        remove_file("Dockerfile_huggingface")
        remove_file(os.path.join("{{cookiecutter.project_slug}}", "index.html"))

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    if "{{cookiecutter.open_source_license}}" == "MIT - MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "GPL-3.0 - GNU General Public License v3":
        move_file("LICENSE_GPL", "LICENSE")
        remove_file("LICENSE_MIT")

    if "{{cookiecutter.open_source_license}}" == "None - Not open source":
        remove_file("LICENSE_GPL")
        remove_file("LICENSE_MIT")

    if "{{cookiecutter.layout}}" == "src":
        if os.path.isdir("src"):
            remove_dir("src")
        move_dir("{{cookiecutter.project_slug}}", os.path.join("src", "{{cookiecutter.project_slug}}"))
