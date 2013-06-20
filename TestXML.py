#!/usr/bin/env python

# -------------------------------
# Unit tests for XML program
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_read_file, ET

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read_file
    # ----

	def test_read_file(self):
		r = "RunXML.in"
		a = 0
		b = xml_read_file(r, a)
		#Found length by printing from XML.py
		self.assert_(len(b) == 246)

	"""
    def test_read (self) :
        #r = "RunXML.in"
        #test_tree = ET.parse(r)
        b = xml_read()
        self.assert_(b.tag    == "THU")

        for child in b:
            print child.tag, child.attrib
	"""        
    
    
    
        
        
    # -----
    # print
    # -----

   # def test_print (self) :
    #    w = StringIO.StringIO()
     #   collatz_print(w, 1, 10, 20)
      #  self.assert_(w.getvalue() == "1 10 20\n")
        
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."


  


