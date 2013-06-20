#!/usr/bin/env python

"""
To run the programXML.out
    % chmod ugo+x RunXML.py
    % RunXML.py < RunXML.in > RunXML.out

To document the program
    % pydoc -w XML
"""

# -------
# imports
# -------

import sys

from XML import xml_read_file, xml_split_roots, xml_data_query

# ----
# main
# ----

xml_read_file(sys.stdin, sys.stdout)
