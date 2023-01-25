#!/usr/bin/env python3

# create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    x=len(configfile.readlines())
    configlist = configfile.readlines()
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print('the number of line =', x)
print(configlist)

