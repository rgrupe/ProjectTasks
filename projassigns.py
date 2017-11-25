"""Project Assignments: Creates a task assignments list by merging a list 
information about projects with a task list template.
Input and output CSV format files.

projassigns.py
version: 2017-11-24
author: Robert Grupe

"""
import csv
import datetime
from pprint import pprint
import sys                  #needed for args

def projects(projectsFile):
    """Import CSV file of information about projects into a dictionary list."""
    with open(projectsFile, 'r') as csvFile:
        global _projsDict
        _projsDict = csv.DictReader(csvFile, dialect="excel")
        
        """Previous code works, but clean table format.
        for row in _projsDict:
            print(row)
            
        print(_projsDict.keys())
        
        for row in range(len(_projsDict)):
            for key, value in _projsDict[row].items():
                print(_projsDict[row][value], end=" ")
            print(" ")
        """    
        print("PROJECTS imported successfully.")
    return

def tasks(tasksFile):
    """ Import template tasks list."""
    return

def assignments():
    """ Combine projects with tasks to create list of assignments."""
    return

def csv_output():
    """ Output assignments list to csv file."""
    return

def main(args): 
    """Receive or request required input files."""
    if (len(args) == 3):
        inputProjects = args[1]
        inputTasks = args[2]
    else:
        print("Please provide the file names you would like to use.")
        inputProjects = input("File name of projects: ")
        inputTasks = input("File name of tasks template: ")
    print("Your are running this program using the projects configuration" + \
          "file {} and the task template file {}.".format(inputProjects, \
          inputTasks) )
#    projects(inputProjects)
#    tasks(inputTasks)
#    assignments()
#    csv_output()
    return

if __name__ == '__main__':
    main(sys.argv)