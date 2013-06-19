#!/usr/bin/env python
import xml.etree.ElementTree as ET

# global Element_Tree
xml_tree = 0

#----------
# xml_read
#----------

def xml_read ():
#def xml_read(s):
	# need to check if it's an empty file or an empty tree
	xml_tree = ET.parse('RunXML.in')
	#xml_tree = ET.fromstring(s)
	xml_root = xml_tree.getroot()
	assert xml_root.tag == 'THU'#print xml_root.tag
	return xml_root

#----------
# xml_read_file
#----------

#def xml_read_singleXMLandQuery
def xml_read_file(r, a) :
	#read lines from in file
	xml_strings = []
	while (r.readline() != "") :
		xml_strings += r.readline()
	#Assumes query is a single line
	xml_query = xml_strings[-1]
	
	for string in range(0, len(xml_strings)-1) :
		tree_string += string 

	#xml_read(tree_string)
	
	
	#tree.fromstring for separate xml trees
