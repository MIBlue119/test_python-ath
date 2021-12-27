# Test Pythopath 


## What is `PYTHONPATH`?

- The default search path for module files
- The only reason to set PYTHONPATH is to maintain directories of custom Python libraries that you do not want to install in the global default location.

Ref:
- [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
- https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html

## Set the `PYTHONPATH` and import the module at the `PYTHONPATH`?

1. Move the module related directories to the PATH which you want to point
2. Use `export PYTHONPATH="$PARENT_PATH_OF_THE_MODULE"` at shell scripts
    - Or add this at bash scripts 
        - If we at Mac, open `~/.bash_profile` and add these
            ```
                export PYTHONPATH="/Users/my_user/code"
            ```
        - If we at Linux, open `~/.bashrc` and add these 
            ```
                export PYTHONPATH=/home/my_user/code
            ```
    - Check whether install successfully
        ```
            echo $PYTHONPATH
        ```
Ref:
- [Using PYTHONPATH](https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html)

## Example

```
.
├── Makefile                # Use makefile to record basic commend
├── README.md
├── foo                     # A module for importing used 
│   ├── __init__.py
│   └── a_module.py
└── scripts                 # Scripts to test module importing
    ├── script_a.py
    └── set_pythonpath.sh   # Shell script to set PYTHONPATH
```

