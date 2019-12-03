# modules are libraries you can import functions from into your python code
# instead of copying and pasting functions and variables from somewhere else
# you can use import command to load from another py file
# you can create your own set of useful functions and then import them
# instead of rewriting stuff
# Some modules are built-in
# search google - list of python modules and pick the official site
# How do you install these externally provided modules?
# They get installed into your Python lib folder
# pip is used to install external modules into your python library in a folder called
# site-packages
# pip3 is the symlink on your mac to run the pip version linked to your python 3.8 installation
#
# Pauls-Mac-mini:bin pauld$ ls -l pip3
# lrwxrwxr-x  1 root  admin  66  2 Nov 16:18 pip3 -> ../../../Library/Frameworks/Python.framework/Versions/3.8/bin/pip3
# 
# YOU MUST ENSURE YOU USE THE RIGHT PIP IN THE RIGHT ENVIRONMENT WHEN INSTALLING
# OTHERWISE YOU COULD END UP WITH INCONSISTENT ENVIRONMENT
#
# YOUR MAC HAS PYTHON 2.7 INSTALLED BY DEFAULT AND APPLE NEED THAT AND USE IT. DONT CHANGE
# IT. THIS WHAT YOU WILL SEE WITH python --version outside of VSCODE
#
#
# IN VSCODE AND PYCHARM YOU CAN USE THE INBUILT OPTIONS TO CHOOSE WHICH PYTHON ENV
# YOU WANT TO USE
#
# PYCHARM IS FROM JETBRAINS AND IS WIDELY USED BY PYTHON ONLY DEVELOPERS
# WHEN CERATING A NEW PROJECT, YOU SELECT WHICH PYTHON INTERPRETER YOU WANT TO USE#
# USE CONFIGURE PREFERENCES TO SETUP YOUR ENV
# 
# pip install <name of module>
#
# you can then use the import directive to use the module in your code
#
# pip uninstall <name of module>
#
