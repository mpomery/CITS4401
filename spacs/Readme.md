#SPACS Readme

SPACS = Swimming Pool Automated Checking System

## Requirements

- Python 2.7 (Python 3 will probably have compatibility issues)

## Instructions

### Configuring

- Run `python [TO IMPLIMENT]` to create a configuration suited to the current machine in `config`
- Alternatively manually copy `spacs.conf.base` to `spacs.conf` and manually set the settings for the machine you would like to run SPACS on.

### Compiling

- Run `python make.py compile` to create `target`
- This will copt all the required files to `target` that are needed to run the application
- Copy  `target` to the server you would like to run it on
- Run python `main.py` on the server from the install directory

### Testing

- Run `python make.py test`
- This will run all tests in `tests`
- Examine the output

## TODO

- Write API
- Write Transaction Bean Handler
- Write Queue Handler

