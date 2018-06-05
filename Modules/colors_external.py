# install the termcoor external package before using it in the file:
# python3 -m pip install termcolor

from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_green", attrs=["blink"])
print(text)
