from enum import auto, unique
from .base_enum import BaseEnum

@unique

class Unit(BaseEnum):
    CELSIUS=auto()
    FAHRENHEIT= auto()

    """This class inherits from the BaseEnum that we just created, and every property is set to
auto(), meaning the value for every item in the enumeration will be set automatically for
us. Since the Unit class inherits from BaseEnum, every time the auto() is called,
the _generate_next_value_ method on BaseEnum will be invoked and will return the
name of the property itself."""
