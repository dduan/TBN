## Development ##

This project is developed with `virtualenv` and Python 3.

Having both installed, the the following steps are necessary to get the
engine running:

    1. Create and enter a virtual environment with `virtualenv`. Note that
    in some environemnt where both Python 2 and 3 are used, using
    `virtualenv -p \`which python3\'` will create a environment where the
    Python packages are shared with the system packages. To fix it, go to the
    `bin` folder in the virtual environment's path, replace the "shebang" of
    every python script in there with the path to the symlink to python in that
    folder.

    2. In top level of the project, run `pip install -r requirements.txt` to
    install dependencies.

    3. Run `py.test` to run all tests.
