#SPACS Readme

SPACS = Swimming Pool Automated Checking System

## Requirements
- Python 2.7 (Python 3 will have compatibility issues)

## Instructions

### Testing

- Run `python make.py test`
- This will run all tests in `tests`
- Examine the output

### Configuring

- Run `python [TO IMPLIMENT]` to create a configuration suited to the current machine in `config`
- Alternatively manually copy `spacs.conf.base` to `spacs.conf` and manually set the settings for the machine you would like to run SPACS on.

### Compiling

- Run `python make.py compile` to create `target`
- This will copt all the required files to `target` that are needed to run the application
- Copy `target` to the server you would like to run it on

### Running

- Run python `main.py` on the server from the target directory

## TODO

Most of this To Do list has been left unfinished due to an unfortunate string of production incidents at work that have eaten into my spare time.
They will be cleaned up before the presentation.

- Finish API
  - Make it so users can only edit what they nare supposed to
- Add PTU Specific Stuff
- Create website front end
- Polish Logging
- Write Configuration Code





