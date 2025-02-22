from abcli.help.generic import help_functions as generic_help_functions

from blue_sandbox import ALIAS
from blue_sandbox.help.blue_sam import help_functions as help_blue_sam


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "blue_sam": help_blue_sam,
    }
)
