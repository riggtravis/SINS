# SINS
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
* All of the logic that uses the models needs to be written.
* Forms need to be used

# Getting Started With SINS

* cd <directory containing this file>
* $VENV/bin/python setup.py develop
* $VENV/bin/initialize_sins_db development.ini
* $VENV/bin/pserve development.ini

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
