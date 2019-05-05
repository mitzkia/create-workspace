import argparse
import logging
import sys
from pathlib import Path

import yaml

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("create_workspace")


def has_content_but_no_file_extension(base_dir, key, value):
    return value and value["content"] and not Path(base_dir, key).suffix


def replace_changeme_if_needed(content, new_string):
    if new_string:
        return content.replace("changeme", new_string)
    return content


def create_parent_dirs_if_needed(base_dir, sub_path, content):
    if Path(base_dir, sub_path).suffix or content is not None:
        Path(base_dir, sub_path).parent.mkdir(parents=True, exist_ok=True)
        logger.info("Directory '%s' has been created", Path(base_dir, sub_path).parent)
    else:
        Path(base_dir, sub_path).mkdir(parents=True, exist_ok=True)
        logger.info("Directory '%s' has been created", Path(base_dir, sub_path))


def create_file_content(base_dir, sub_path, content):
    if Path(base_dir, sub_path).suffix or content is not None:
        with open(Path(base_dir, sub_path), "w") as file_object:
            file_object.write(content)
            logger.info("File '%s' has been created with content", Path(base_dir, sub_path))


def create_workspace(input_file, replace_string=None):
    with open(input_file, "r") as file_object:
        yaml_content_as_dict = yaml.safe_load(file_object)

    if "base_dir" not in yaml_content_as_dict.keys():
        logger.error("Definition of 'base_dir' must be exist in input file: %s", input_file)
        sys.exit()

    for key, value in yaml_content_as_dict.items():

        if key == "base_dir":
            base_dir = value
            continue

        key = replace_changeme_if_needed(key, replace_string)
        if value and value["content"]:
            value["content"] = replace_changeme_if_needed(value["content"], replace_string)

        create_parent_dirs_if_needed(base_dir, key, value["content"])

        if value:
            create_file_content(base_dir, key, value["content"])


def main():
    parser = argparse.ArgumentParser(description="Tool which can create dirs and files from yaml")
    parser.add_argument("--input", help="YAML formatted input file")
    parser.add_argument("--replace", help="The new string when replacing")
    args = parser.parse_args()

    input_file = args.input
    replace_string = args.replace
    create_workspace(input_file=input_file, replace_string=replace_string)


if __name__ == "__main__":
    exit(main())
