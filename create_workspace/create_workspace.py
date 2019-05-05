import argparse
import logging
from pathlib import Path

import yaml

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("create_workspace")


def replace_changeme_if_needed(pattern, replace_string):
    if replace_string:
        if pattern and pattern:
            # We have a file content
            return pattern.replace("changeme", replace_string)
        # We have a path
        return pattern.replace("changeme", replace_string)
    # There is no replace string defined
    return pattern


def create_parent_dirs(base_dir, defined_path, content):
    if content is not None:
        # File is specified
        Path(base_dir, defined_path).parent.mkdir(parents=True, exist_ok=True)
        logger.info("Directory '%s' has been (re-)created", Path(base_dir, defined_path).parent)
    elif not content:
        # Dir is specified
        Path(base_dir, defined_path).mkdir(parents=True, exist_ok=True)
        logger.info("Directory '%s' has been (re-)created", Path(base_dir, defined_path))


def create_file_content(base_dir, defined_path, content):
    if content is not None:
        # File is specified
        with open(Path(base_dir, defined_path), "w") as file_object:
            file_object.write(content)
            logger.info("File '%s' has been created with content", Path(base_dir, defined_path))


def create_workspace(base_dir, input_file, replace_string=None):
    with open(input_file, "r") as file_object:
        yaml_content_as_dict = yaml.safe_load(file_object)

    for defined_path, file_content in yaml_content_as_dict.items():

        defined_path = replace_changeme_if_needed(defined_path, replace_string)
        file_content = replace_changeme_if_needed(file_content, replace_string)

        create_parent_dirs(base_dir, defined_path, file_content)
        create_file_content(base_dir, defined_path, file_content)


def main():
    parser = argparse.ArgumentParser(description="Tool which can create dirs and files from yaml")
    parser.add_argument("--base-dir", required=True, help="The base path for created workspace")
    parser.add_argument("--input", required=True, help="YAML formatted input file")
    parser.add_argument("--replace-string", help="The new string when replacing")
    args = parser.parse_args()

    base_dir = args.base_dir
    input_file = args.input
    replace_string = args.replace_string
    create_workspace(base_dir=base_dir, input_file=input_file, replace_string=replace_string)


if __name__ == "__main__":
    exit(main())
