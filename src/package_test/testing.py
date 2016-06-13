'''
Created on Jun 13, 2016

@author: jeanpaul.iradukunda
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        print 
        print "**************************************"
        print "Testing in: %s" % self._testMethodName 
        print "**************************************"
        pass


    def tearDown(self): 
        pass


    def testName(self):
        print "Hello World - just getting started!"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 