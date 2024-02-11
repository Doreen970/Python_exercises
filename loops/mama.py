#!/usr/bin/python3
from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Please choose color either 'red', 'green', or 'blue' "))

match color:
    case Color.RED:
        print("You have entered red")
    case Color.GREEN:
        print("You chose green")
    case Color.BLUE:
        print("You entered blue")
    case _:
        print("no selection from list")
