# rock-paper-scissors-game
This is an interactive rock, paper, scissors game where the user competes against the computer.

# Prerequisities
Anaconda 3.7+
Python 3.7+
Pip

# Installation
Fork this [remote repository] (https://github.com/prof-rossetti/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

cd Desktop
cd rock-paper-scissors-game

Use Anaconda to create and activate a new virtual environmnt, perhaps called "my-first-env":

conda create -n my-first-env python=3.8
conda activate my-first-env

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

pip install -r requirements.txt

>NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

# Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file afterwards):

    USER_NAME="Jon Snow"
    SECRET_PASSWORD="super duper secret"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

# Usage

Run the Python script:

python app/game.py

# alternative module-style invocation (only required if importing from one file to another):
python -m app.my_script

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.