#!/usr/bin/env python3
from pwn import *
import click

####################
# Challenge Server #
####################

SERVER = "the.server.goes.here"
PORT = 1337


def exploit():
    # Payload start...
    payload = b'A' * 64  # Padding
    payload += pop_rdx

    # Pwn here...

    assert len(payload) <= 2702  # Max payload size in the challenge
    p.recvuntil(b':')
    p.sendline(payload)
    p.interactive()


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument(
    "binary",
    required=False,
    default=None,
    type=click.Path(exists=True)
)
@click.option(
    "-np", "--no-pause",
    is_flag=True,
    default=False,
    type=click.BOOL,
    help=("Do not pause the program when started. "
          "Off by default, ignored if connecting to a server.")
)
def start_exploit(binary, no_pause):
    """
    Connect to the server or binary and call the exploit.

    If given a local binary to exploit, run the exploit locally.
    Otherwise, connect to a remote server.
    """
    global p
    p = process([binary]) if binary else remote(SERVER, PORT)

    # Pause the process and show the PID giving time for a debugger to attach
    if not no_pause and binary:
        click.echo(f"[+] PID: {util.proc.pidof(p)}")
        pause()

    exploit()
    click.echo("[*] Exiting...")
    p.kill() if binary else p.close()

# Pwntools now uses pwn.toplevel
#if __name__ == "__main__":
start_exploit()
