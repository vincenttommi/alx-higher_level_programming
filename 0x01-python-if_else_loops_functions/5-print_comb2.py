#!/usr/bin/python3

"""Print numbers 0 to 99 separated by ',' followed by a space."""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:2}".format(number),end=",")    