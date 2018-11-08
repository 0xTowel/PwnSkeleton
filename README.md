# Pwn Skeleton for Python3
A small, template-like example script for doing binary exploitation in Python3.

## Requirements
The script uses:
  * [Python3](https://www.python.org)
  * [Click](https://click.palletsprojects.com/en/7.x)
  * [Pwntools Full 3 Compat by Arusekk](https://github.com/Arusekk/pwntools/tree/full-3-compat)
  
## Installing Pwntools Full 3 Compat
As listed in the requirements, you will need [Pwntools Full 3 Compat by Arusekk](https://github.com/Arusekk/pwntools/tree/full-3-compat) for Python3 support. The following instructions will install this forked branch for the current user:

```
$ git clone -b "full-3-compat" https://github.com/Arusekk/pwntools.git
$ cd pwntools
$ python3 setup.py install --user
```
If everything worked okay running `python3 -c 'from pwn import *'` should not give any errors and exit cleanly.

## Usage
The script tries connects to a server if no binary is passed as an argument. It also supports
pausing the binary and listing the PID to give time for a debugger to attach.

```
Usage: solve.py [OPTIONS] [BINARY]

  Connect to the server or binary and call the exploit.

  If given a local binary to exploit, run the exploit locally. Otherwise,
  connect to a remote server.

Options:
  -np, --no-pause  Do not pause the program when started. Off by default,
                   ignored if connecting to a server.
  -h, --help       Show this message and exit.
```

## Development and Future Work
This is just a simple template script designed to be user-friendly, hackable, and most of all useful.
As a result, if there's something you believe would improve it please submit a PR.
