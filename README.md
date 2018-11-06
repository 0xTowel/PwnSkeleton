# Pwn Skeleton for Python3
A small, template-like example script for doing binary exploitation in Python3.

## Requirements
The script uses:
  * [Python3](https://www.python.org)
  * [Click](https://click.palletsprojects.com/en/7.x)
  * [Pwntools Full 3 Compat by Arusekk](https://github.com/Arusekk/pwntools/tree/full-3-compat)

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
