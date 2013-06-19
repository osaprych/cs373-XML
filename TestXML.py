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

from XML import XML_read, XML_solve, ET

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
	r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
	test_tree = ET.parse(r) 
	b = xml_read(r, test_tree)
        self.assert_(b    == True)
        self.assert_(test_tree ==  True)
        #self.assert_(a[1] == 10)
        
        
    
    
    
        
        
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


  


