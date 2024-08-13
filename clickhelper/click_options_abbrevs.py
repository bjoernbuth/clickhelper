"""Module containg several click options used at several places
that are therefore defined here to avoid redundancy."""

import click
from functools import wraps
from pprint import pprint


help_shorter_option = click.help_option("--help", "--h")


PRINT_OFF_OFF = None

print_off_option = click.option(
    "--print_result-off",
    "--po",
    help="print off - Do NOT print the result to the console.",
    default=False,
    show_default=True,
    is_flag=True,
)


PRINT_RESULT = None
print_result_option = click.option(
    "--print_result/--nop",
    "--p/--q",
    help="Print the result to the console.",
    default=True,
    # default=False,
    show_default=True,
    is_flag=True,
)


NON_RECURSIVE = None
non_recursive_option = click.option(
    "--non_recursive",
    "--nr",
    is_flag=True,
    default=False,
    show_default=True,
    help="Do not recurse into subdirs.",
)
