"""Module containg several click options used at several places
that are therefore defined here to avoid redundancy.

Options: (In brackets the name of the parameter in the function)

All the option 'factories' mentioned here contain one extra parameter named
default_value whose meaning is clear from the context.

- copy_to_clipboard_option: Option to copy the result of the command to the clipboard
  (copy_to_clipboard)
- help_shorter_option: Shorter help option (print_result).
- print_off_option: Option to not print the result to the console (print_off_option).

Option factories:
- orientation_option factory: Option to set the orientation of the graph (orientation).
- print_option_factory: Option to print the result to the console (print_result).
"""

import click
from functools import wraps
from pprint import pprint


help_shorter_option = click.help_option("--help", "--h")
# @click.help_option("--help", "--h". "--aaa")

copy_to_clipboard_option = click.option(
    "--copy_to_clipboard/--noc",
    "-c",
    is_flag=True,
    default=True,
    show_default=True,
    help="Copy the result of the command to the clipboard.",
)


PRINT_OFF_OFF = None

# TODO0 replace by factory
print_off_option = click.option(
    "--print_result-off",
    "--po",
    help="print off - Do NOT print the result to the console.",
    default=False,
    show_default=True,
    is_flag=True,
)

# print_output_option = click.option(
#     "--print_output/--no-print",
#     "--p/--nop",
#     is_flag=True,
#     default=True,
#     show_default=True,
#     help="Print result to console.",
# )

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


def print_function_signature(f):
    """Print the signature of the function f."""
    import inspect

    print()
    # print the name of the function
    print(f.__name__)
    arguments = str(inspect.signature(f)).split(",")
    for arg in arguments:
        print("\t" + arg)
    # print(str(inspect.signature(f)).split(","))
    print()


# TODO0 remove this constant later aftter debugging (if it feels right)
DEBUG = True
debug = DEBUG


def print_option_factory(default_value=False):
    return click.option(
        "--print_result",
        "--p",
        is_flag=True,
        default=default_value,
        show_default=True,
        help="Print the result to the console.",
    )


def orientation_option_factory(*args, default_value="TD"):
    """Click option factory for the orientation of the graph.

    "orientation" will be added to the list of args if it is not already there.

    Args:
        *args: The list of names for the option in the command line. E.g. "orientation", "or1". They
        will get double dashes added to them.

        default_value: The default value for the option.
    """
    # print(args)
    new_args_list = list(args)
    # check if "--orientation" is in the list of args and if not add it at the beginning
    if "orientation" not in new_args_list:
        new_args_list.insert(0, "--orientation")

    return click.option(
        # "--orientation",
        *new_args_list,
        default=default_value,
        show_default=True,
        help="Orientation of the graph, TD/LR. Default is TD.",
    )
