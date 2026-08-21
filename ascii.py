from termcolor import colored
import pyfiglet


def modify():
    text = input("What message do you want to print? \n")
    color = input("What color? \n")
    colors = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",                       
            "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue",     
            "light_magenta", "light_cyan")
    if color not in colors:
        color = "cyan"
        print("You did not enter any color!")
    result = text.upper()
    result = pyfiglet.figlet_format(result)
    result = colored(result, color)

    return result


print(modify())
