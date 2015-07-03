#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'Ritesh Shah (ritesh.shah@imag.fr)'
__copyright__ = 'Copyright (c) 2014-2015 Ritesh Shah'
__license__ = 'New-style BSD'
__vcs_id__ = '$'
__version__ = '1.2.3'  #Versioning: http://www.python.org/dev/peps/pep-0386/

### Imports ###


### Begin code ###

def featCommaSepList():
    """
    Feature to capture single tokens separated by atleast two commas.
    For instance:
        "delhi , mumbai , jaipur"
        "delhi , mumbai , chandigarh , gandhinagar"
    Args:
        normText: sequence of normalised tokens (where token, single whitespace separated character sequence)

    Returns:

    """
    return None


def justForTest( N ):
    return N


### Unit Testing ###
import unittest

class TestMyMethods(unittest.TestCase):

    def testCommaSepList(self):
        self.assertEqual(featCommaSepList(), None)
        self.assertNotEqual(featCommaSepList(), 1)

    def testCommaSepList2(self):
        self.assertEqual(featCommaSepList(), None)
        self.assertNotEqual(featCommaSepList(), 1)

    def testJustForTest(self):
        self.assertEqual(justForTest(5), 5)
        self.assertNotEqual(justForTest(10), 5)

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)