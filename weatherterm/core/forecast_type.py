#an enumeration to represent each option of the weather forecast
from enum import Enum, unique

@unique
class ForecastType(Enum):
    #we have values for the four types of forecast that the application will provide, and where values such
    #as ForecastType.TODAY, ForecastType.WEEKEND, and so on can be accessed.
    TODAY= 'today'
    FIVEDAYS='5day'
    TENDAYS='10day'
    WEEKEND='weekend'

    #note that we are assigning constant values that are different from the
    #the property item of the enumeration, the reason being that later these values will be used
    #to build the url to make requests to the weather website
