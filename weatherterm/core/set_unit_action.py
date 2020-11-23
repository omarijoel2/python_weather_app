from argparse import Action

from weatherterm.core import Unit


class SetUnitAction(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        unit = Unit[values.upper()]
        setattr(namespace, self.dest, unit)
#this action class is very simple; it just inherits from argparse.action and overrides the __call__ method.
#
