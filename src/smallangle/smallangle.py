import click
import numpy as np
import pandas as pd
from numpy import pi

# making a group of commands
@click.group()
def cmd_group():
    pass

# creating a command for options
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of steps between 0 and 2pi",
    show_default=True,  # show default in help
)

# creating a command for calculating the sine
@cmd_group.command()
# @click.argument("number")
def sin(number):
    """Calculate sin(x) between a given boundary over a number of steps.

    Args:
        number (integer): steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# creating a command for options
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of steps between 0 and 2pi",
    show_default=True,  # show default in help
)

# creating a command to calculate the tan
@cmd_group.command()
# @click.argument("number")
def tan(number):
    """Calculate tan(x) between a given boundary over a number of steps.

    Args:
        number (integer): steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

# calling function with command
if __name__ == "__main__":
    cmd_group()
