#!/usr/bin/env python
import xml.etree.ElementTree as ET

# global Element_Tree
xml_tree = 0

#----------
# xml_read
#----------

def xml_read ():
	# need to check if it's an empty file or an empty tree
	xml_tree = ET.parse('RunXML.in')
	xml_root = xml_tree.getroot()
	assert xml_root.tag == 'THU'#print xml_root.tag
	return xml_root
#----------
# xml_print
#----------

"""
def xml_solve(r, w) :

	xml_read(r, xml_tree) 
"""