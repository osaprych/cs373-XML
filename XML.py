#!/usr/bin/env python
import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import ElementTree

# global Element_Tree
#xml_tree = ElementTree()

#----------
# xml_read
#----------

def xml_split_roots(s):
	#Get root element of newly created tree
	root_from_string = ET.fromstring(s)
		
	#Create list of children
	xml_children_list = []
	for xml_child in root_from_string :
		print "child is "
        	#print root_from_string
		print xml_child
		xml_children_list += xml_child
	
	print xml_children_list
		
	
	
	#ET.ElementTree(root_from_string).write(xml_temp.in)
	#xml_tree = ET.fromstring(s)
	#xml_root = xml_tree.getroot()
	
	#print xml_root

	#return xml_root


#----------
# xml_read_file
#----------

#def xml_read_singleXMLandQuery
def xml_read_file(r, a) :
	#Open file
	#xml_file = open('RunXML.in')
	xml_file = open(r)
	#Read entire file
	xml_file_string = xml_file.read()
	#Concatenation of void xml tags around entire input
	xml_file_string = "<xml>" + xml_file_string + "</xml>"
	print xml_file_string
	assert len(xml_file_string) > 0

	xml_split_roots(xml_file_string)

	return xml_file_string
