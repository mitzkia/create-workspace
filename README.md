# create-workspace

* The goal of this project to create a workspace (directories and files) from a pre-defined YAML file.

* When will be this useful?
  * When you want to design a workspace
  * When automatic workspace creation is a solution

## Use case

* Let assume we have a following YAML file
* This example demonstrates:
  * creating sub directories
  * creating files with contents
  * replacing strings within created template

```yaml
base_dir: /home/myuser/mydir/

first-level-dir1/second-level-dir1/:

first-level-dir2/second-level-dir2/test-file.txt:
  content: "example content line 1\n\
example content line 2\n\
"

first-level-dir3/changeme/test-file.txt:
  content: "changeme\n\
"
```

* We can execute `create-workspace` in a following way

```bash
$ python3 create_workspace/create_workspace.py --input example/example-workspace.yml --replace custom-content
INFO:create_workspace:Directory '/home/myuser/mydir/first-level-dir1/second-level-dir1' has been created
INFO:create_workspace:Directory '/home/myuser/mydir/first-level-dir2/second-level-dir2' has been created
INFO:create_workspace:File '/home/myuser/mydir/first-level-dir2/second-level-dir2/test-file.txt' has been created with content
INFO:create_workspace:Directory '/home/myuser/mydir/first-level-dir3/custom-content' has been created
INFO:create_workspace:File '/home/myuser/mydir/first-level-dir3/custom-content/test-file.txt' has been created with content
```

* The following directory and file structure will be created

```bash
$ tree
.
├── first-level-dir1
│   └── second-level-dir1
├── first-level-dir2
│   └── second-level-dir2
│       └── test-file.txt
└── first-level-dir3
    └── custom-content
        └── test-file.txt

6 directories, 2 files

$ cat first-level-dir2/second-level-dir2/test-file.txt
example content line 1
example content line 2

$ cat first-level-dir3/custom-content/test-file.txt
custom-content
```
