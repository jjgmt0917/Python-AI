import pyfiglet
from termcolor import colored

# py_text = pyfiglet.figlet_format("Hello")
# color_text = colored(py_text, "red")
# print(color_text)

# py_text = pyfiglet.figlet_format("Python")
# color_text = colored(py_text, "yellow", "on_blue", ["bold"])
# print(color_text)


final_text  = colored(pyfiglet.figlet_format("Hello Python"), "green", "on_blue", ["bold"])
print(final_text)