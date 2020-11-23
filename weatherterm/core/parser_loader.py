import os
import re
import inspect

#a function that when executed returs a list of all files located in weathermterm/parsers
#it will filter the files based on the rules
def _get_parser_list(dirname):
    files = [f.replace('.py', '')
    for f in os,listdir(dirname)
    if not f.startswith('__')


    ]
    return files

#after importing the files it's time to import the module
"""The inspect.getmembers function returns a list of tuples where the first item is a key
representing a property in the module, and the second item is the value, which can be of
any type. In our scenario, we are interested in a property with a key ending with
parser and with the value of type class."""
def _import_parsers(parserfiles):
    m= re.compile('.+parser$', re.I)

    _modules= __import__('weatherterm.parsers',
                          locals(),
                          globals(),
                          parserfiles,
                          0
                          )
    _parsers=[(k,v) for k, v in inspect.getmembers(_modules)
               if inspect.ismodule(v) and m.match(k)]

    _classes=dict()
    """Lastly, we loop through the items in the module and extract the parser classes, returning a
dictionary containing the name of the class and the class object that will be later used to
create instances of the parser."""

    for k,v in _parsers:
        __classes.update({k: v for k, v in inspect.getmembers(v)
                          if inspect.isclass(v) and m.match(k)})

    return _classes
def load(dirname):
    parserfiles= _get_parser_list(dirname)
    return _import_parsers(parserfiles)
