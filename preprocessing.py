#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'Ritesh Shah (ritesh.shah@imag.fr)'
__copyright__ = 'Copyright (c) 2014-2015 Ritesh Shah'
__license__ = 'New-style BSD'
__vcs_id__ = '$Id$'
__version__ = '1.2.3'  # Versioning: http://www.python.org/dev/peps/pep-0386/

### Begin code ###

import re, codecs


def test():
    """ Testing Docstring"""
    pass

def normalise(rawTextList):
    """
    Function for normalising text.
    1.  For each string in the list, squeezes all kinds of spaces withing the string to a single whitespace and
        trims each string
    2.  Do we need to handle empty lines? Correspondences in both src and tgt will then have to be checked
    :arg: (List)
    Args:
        rawTextList: list of newline separated strings
    :rtype : (List)
    Returns:
        normTextList: list of normalised newline separated strings
    """
    normTextList = []
    for r in rawTextList:
        nr = re.sub(u'\s+', ' ', r)
        normTextList.append(nr.strip())
    return normTextList

def readBiCorpus(srcLangFPath, tgtLangFPath):
    """
    Function which reads parallel corpus from two files, makes basic checks like alignments etc.
    :arg : (String,String)
    Args:
        srcLangFile: file path containing source language corpus
        tgtLangFile: file path containing target language corpus
    :rtype : (Tuple)
    Returns:
        A tuple of two lists
    """

    fSrc = codecs.open(srcLangFPath, 'rb', 'utf8')
    fTgt = codecs.open(tgtLangFPath, 'rb', 'utf8')
    fsList = fSrc.readlines()
    ftList = fTgt.readlines()
    if len(fsList) == len(ftList):
        print fsList[0:4]
        print ftList[0:4]
    else:
        print("Length mismatch in bilingual corpus")
    return normalise(fsList), normalise(ftList)

if __name__ == '__main__':
    test()