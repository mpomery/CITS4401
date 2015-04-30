#SPACS Readme

SPACS = Swimming Pool Automated Checking System

This file is a quick guide for running the SPACS system, with technical notes that did not
fit into the report at the bottom.


## Requirements
- Python 2.7 (Python 3 will have compatibility issues)

## Instructions

### Testing

- Run `python make.py test`
- This will run all tests in `tests`
- Examine the output

### Configuring

- Run `python [TO IMPLIMENT]` to create a configuration suited to the current machine in
  `config`
- Alternatively manually copy `spacs.conf.base` to `spacs.conf` and manually set the settings
  for the machine you would like to run SPACS on.

### Compiling

- Run `python make.py compile` to create `target`
- This will copt all the required files to `target` that are needed to run the application
- Copy `target` to the server you would like to run it on

### Running

- Run python `main.py` on the server from the target directory

## TODO

Most of this To Do list has been left unfinished due to an unfortunate string of production
incidents at work that have eaten into my spare time. They will be cleaned up before the
presentation.

- Finish API
  - Make it so users can only edit what they nare supposed to
- Add PTU Specific Stuff
- Create website front end
- Polish Logging
- Write Configuration Code

## Things To Take Note Of

This is my personal reflection of the unit. The stuff here didn't seem to fit into the report
anywhere. I saw the report as something I would hand over to a client to show them we were
going to provide them exactly what they want. Information here is more something I would state
internal to the organization that I was working for.

### TransactionBean.py

This file is where a lot of the initial development time was spent. Managed Tranasctions
have been in Java since before Java 5 and are used to manage database reading and writing
in enterprise applications. I have had very little personal experience with them, but recognize
that they are integral to many successful applications.

Writing this class was eye opening

This is the part of the code base I am most proud of. I plan on polishing it up, making it
more generic and releasing it back to the python community.

### Python as a language choice

In hindsight, python was probably not the best language choice for this project. Not because of
it's inablilty to do things, but because it hasn't been used in many enterprise applications
previously. I saw this as a good opportunity to try it out for myself and push python to the
limits. The code I have written is less pretty than I would have liked, but a whole lot prettier
than what I have written previously.

While working in this project, I listened to the talks from PyCon 2015. I would recommend them
to anyone looking to learn python. One of the talks talked about python's multithreading ability.
Unfortunately it works differently to what I thought, and so won't run as fast as I would expect under
heavy load. Fortunately the statelessness means that more servers can be started to deal with load issues.













