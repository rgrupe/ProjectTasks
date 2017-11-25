# projassigns

Project Assignments: Creates an assignment list from a list of information about projects and a template list of project tasks.
Input and output information through CSV format files.

Primary initial use is for uploading multiple projects' tasks into Jira.

## Usage

$ python projassigns.py projects.csv tasks.csv


## Development Status

In-work initial development.

## To Do
1. TDD: Test Driven Development  
  1.1 doctest functional tests: test/projassigns_test.txt  
  1.2 unittest unit tests
2. Complete functionality from POC exercise.
3. Eliminate use of global variables??
4. Combine importing of projects and tasks into a single function.
5. Add Jira API integration.


## Running the tests

See [Test README.md](test/README.md)

## Authors

* **Robert Grupe** - *Initial work* - [rgrupe](https://github.com/rgrupe)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details