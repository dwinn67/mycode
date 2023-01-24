#!/usr/bin/env python3
# Alta3 Research || Author: RZFeeser@alta3.com
# Check hostname against expected value

def main():

    #User imput hostname
    hostname = input("What value should we set for hostname?")
    
    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    print ("Exiting the script.")

main()

