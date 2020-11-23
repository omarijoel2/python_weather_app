#the application needs one more enumeration to represent the temperature units that the
#user will be able to choose from in the command line. this enum will contain celsius & fahreinheit

from enum import Enum

class BaseEnum(Enum):
    def _generate_next_value_(name,start, count, last_value):
        return name
