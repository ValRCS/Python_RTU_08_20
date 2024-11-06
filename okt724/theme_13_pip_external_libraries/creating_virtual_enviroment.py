# virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
# In this example, we will create a virtual environment in the project directory.
# To create a virtual environment, we use the venv module.
# The venv module provides support for creating lightweight "virtual environments" with their own site directories, optionally isolated from system site directories.
# The venv module is included in the Python standard library and requires no additional installation.
# To create a virtual environment, we use the venv module.

# let's create a virtual environment
# from command line:
# python -m venv myenv
# myenv could be any name you want to give to your virtual environment
# This command creates a directory called myenv in the current directory.
# it copies the Python interpreter and standard library into the myenv directory.
# It also creates a site-packages directory inside the myenv directory.

# now let's activate the virtual environment
# from command line:
# source myenv/bin/activate (Linux)
# myenv\Scripts\activate (Windows)

# now you can install packages in the virtual environment
# using pip install package_name
# can list all installed packages using pip freeze
# can deactivate the virtual environment using deactivate command

# finally we can fix our library versions in a requirements.txt file
# from command line:
# pip freeze > requirements.txt

# on a new computer, we can install all the required packages using the following command
# pip install -r requirements.txt