# Django blueprint app
PyCharm will prepare the virtual environment for project automatically. For non-PyCharm users (for example VSCode) look an instructions below how to do this manually

## How to run local server
Get to the `webapp` directory: `cd webapp` and run `python3 manage.py runserver` from webapp folder

*In some enviroments it could be not `python3` but `python`* 


### How to set up a virtual environment:

`python3 -m venv .venv` and then select new environment in a VSCode (bottom-right corner)

### How to switch to a virtual environment in a terminal

On Windows: Run `.venv\Scripts\Activate`. Then you will see (.venv) on the left from a CLI prompt.

On macOS: Run `source .venv/bin/activate`. Then you will see (.venv) on the left from a CLI prompt.
If you have a Python extension installed on your Visual Studio Code, it can try to run `source .venv/bin/activate` command on its own right after terminal opening.

### How to install all dependencies in an env

`pip3 install -r requirements.txt`

### How Quit the server :
Quit the server with CTRL-C in command line

## Happy coding!
