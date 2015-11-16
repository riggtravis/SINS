# SINS

[![Join the chat at https://gitter.im/riggtravis/SINS](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/riggtravis/SINS?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
SINS is not SFIM

## Well if it's not SFIM then what is it?
It's forum software based on SFIM. In fact it's the reference implementation of
SFIM. It is built using Python because Python is readable. It is based on
Pyramid because Pyramid is flexible. It uses Mako because Mako is readable. It
uses SQLalchemy because SQLalchemy is easy.

## Okay, but what exactly is SFIM?
[SFIM](https://github.com/riggtravis/SFIM) is a forum standard that is intended
to be well document and easy to build interfaces for. The dream of SFIM is to
allow users to interact with SFIM based forums in consistent ways while SFIM
implementers can use languages that they are comfortable with using tools that
offer different experiences in terms of responsiveness. The ultimate goal is to
allow for smartphone apps that can easily interact with SFIM based forums.

# What is done?
* The database models are written.
* Templates are using bootstrap

# What is left to do?
* Most of the logic that uses the models needs to be written.
* Forms need to be used

# Getting Started With SINS
## For contributors:
1. Make sure python is installed on your system.
2. Create a directory for a virtual environment. An example of what this might be like is "web-app"
3. Run the following command
    python easy_install virtualenv
4. Change directories into the directory you created for your virtual environment.
5. Clone this repository in the usual way. Make sure that SINS resides in a directory inside of the virtual environment directory.
6. The directory for the virtual environment will from now on be referred to as $VENV. If you cannot create a session variable for whatever reason, replace $VENV with the path to this directory.
7. Run these commands:

        cd $VENV/sins                                 <- This might be SINS
        $VENV/bin/python setup.py develop

## Running
SINS is not currently in a state where it can run. It also needs to be run in a virtual environment. For this, follow
the instructions that have been provided to contributors all the way to step six. Instead of step seven, run the
following commands:

        cd $VENV/sins
        $VENV/bin/python setup.py
        $VENV/bin/initialize_sins_db production.ini

# Licensing
SINS is available under an MIT license.

# Credits
Special thanks go to Cody N Vaughn for helping me design a few of the non SFIM
dictated portions of this program. He was much more help than he probably
ever realized.

More thanks also go to Brock Jahnke, who helped me design SFIM and helped me
figure out what the key features for SINS should be.

Also thanks to Jan Pierce, who gave me a reason to see this project through to
the end. It may not be there yet, but if it does get there it will be because of
the opportunity I have been given.
