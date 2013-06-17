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

#from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle, cache

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    #def test_read (self) :
     #   r = StringIO.StringIO("1 10\n")
      #  a = [0, 0]
       # b = collatz_read(r, a)
        #self.assert_(b    == True)
        #self.assert_(a[0] ==  1)
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


  


