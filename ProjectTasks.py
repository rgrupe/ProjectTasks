"""Exercise program for combining a list of projects with a template list of tasks to produce a list project team member assignments.

version: 2017-11-22
author: Robert Grupe

TODO: 
1. unittest so can run application from IDE console
2. doctest details (examples of running application): $ python3.6 -m doctest -v proj_assigns.py <-- Needs to be a package??
3. No use of global ?? (test in exercise.
"""
import csv
import datetime
from pprint import pprint
import sys                  #For Args

def projects(projectsFile):
    """ Import list of projects with information about each into dictionary list.
    
    >>> from proj_assigns import projects
    >>> projects(project.csv)
    PROJECTS
    >>> 

    """
    with open(projectsFile, 'r') as csvFile:
        global _projsDict
        _projsDict = csv.DictReader(csvFile, dialect="excel")
        print("PROJECTS")
        
        """Previous code works, but clean table format.
        for row in _projsDict:
            print(row)
        """
            
        print(_projsDict.keys())
        """
        for row in range(len(_projsDict)):
            for key, value in _projsDict[row].items():
                print(_projsDict[row][value], end=" ")
            print(" ")
        """    
    return

def tasks(tasksFile):
    """ Import template tasks list. """
    return

def assignments():
    """ Combine project details with template tasks to create list of assignments."""
    return

def csv_output():
    """ Output assignments list to csv file. """
    return

def main(args):
    """ Receive or request required input files. 
    
        >>> from proj_assigns import main
        >>> projects(project.csv, tasks.csv)
        Using project file project.csv, and tasks template tasks.csv.
        >>> 

    """
    if (len(args) == 3):
        print("Using project file {} and task template {}.".format(args[1], args[2]) )
        inputProjects = args[1]
        inputTasks = args[2]
    else:
        print("Please provide the file names you would like to use.")
        inputProjects = input("File name of projects: ")
        inputTasks = input("File name of tasks template: ")
    projects(inputProjects)
#    tasks(inputTasks)
#   assignments()
#   csv_output()
    return

if __name__ == '__main__':
    main(sys.argv)