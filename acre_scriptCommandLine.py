"""
For longer comments, put them inside triple quotes.
Everything inside the triple quotes will be ignored.

MAIN COMMENT

The main comment should explain what the script does and give
any information that someone would need to run the script, 
such as what type of files are required (if any).

For this script:
This script converts plot size from length, width to acres.

This script takes a comma-separated file with an address or 
other identifier in the first column, plot width in feet in 
the second column, and plot length in feet in the third column.


To run the script:
This script can be run from the command line. This file does 
not need to be open to run the script on the command line.
Run the script on the command line by navigating to the
folder that contains this script and the data file and
typing python acre_script.py.
Alternatively, you can run the script from anywhere by
using the absolute path. The absolute path depends on where
you saved the files.
"""

#IMPORT MODULES
#if you have any modules to import, import them at the top of the script,
#under the comments, so that anyone using this script can quickly
#know which modules are required - they might need to install them.
#These are called dependencies.
import sys

#HARD-CODED VARIABLES
#assign any variables, including filenames, here, so that if you want to
#run the script with different data, it's easy to see and change
file_name = sys.argv[1]

#FUNCTION DEFINITIONS
#include any function definitions next
def sqft_to_acres(sqft):
    #this function takes square footage and returns rounded acreage
    acres = sqft / 43560
    return round(acres, 2)
    
#DEFINE MAIN FUNCTION
#This is where you put most of your code, including any function calls
def main():
	with open(file_name, "r") as f:
		plots = {line.split(",")[0]: float(line.split(",")[1]) * float(line.split(",")[2]) for line in f.readlines()}
	for address, value in plots.items():
		answer = sqft_to_acres(value)
		print(address + " is " + str(answer) + " acres.")

#CALL MAIN
#We call main this way so that we can also use the individual functions
if __name__ == "__main__":
	main()




        
