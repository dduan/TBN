## Running the App ##

This project depends on Python version 3+ and `pip`, the Python package management program.

To run the app, make sure `pip3` works properly with Python 3. Then:

    * run `pip3 install -r requirements.txt` to install all dependencies listed in requirements.txt
    * start the server by `python3 start_server.py`
    * open a local browser and visit `http://localhost:5000`

## Testing ##

After all dependencies are satisfied, use the command `py.test` under project root will run all the tests.

Currently the test `test_known_units` fails on Windows machines due to a text encoding error for the degree symbol. It passes on Unix systems.