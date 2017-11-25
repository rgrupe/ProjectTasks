""" Test module for projectassigns.py

version: 2017-11-24
author: Robert Grupe
"""
import unittest
import projassigns.py

class TestCase00(unittest.TestCase):
    """Tests for `ProjectTasks.py`."""

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print("TestCase00:setUp_:begin")
        ## do something...
        print("TestCase00:setUp_:end")
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print("TestCase00:tearDown_:begin")
        ## do something...
        print("TestCase00:tearDown_:end")
     
    # test function projects
    def testA(self):
        """Test function projects"""
        print("TestCase00:projects")
     

if __name__ == '__main__':
    unittest.main()
