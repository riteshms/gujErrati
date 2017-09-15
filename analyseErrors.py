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

#
#
import prelimFeatures, preprocessing

if __name__ == '__main__':
    biList=preprocessing.readBiCorpus('resources/bicorpus.en','resources/bicorpus.gu')
    print biList


