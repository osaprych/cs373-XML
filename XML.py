#!/usr/bin/env python
import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import ElementTree

# global Element_Tree
#xml_tree = ElementTree()
counter = [1]	

#----------
# xml_data_query
#----------

def depth_search(parent) :
	for child in parent :

		child.set(child.tag, counter[0])
		counter[0] += 1
		#print parent
		print child.attrib
		depth_search(child)


#----------
# xml_get_subelements
#----------

def xml_get_subelements(d, q) :
	d.set(d.tag, counter[0])
	counter[0] += 1
	depth_search(d)
	# parsing subtree

#----------
# xml_data_query
#----------

def xml_data_query(xml_list) :
	data = xml_list[0] # XML documents with exactly one root element 
	query = xml_list[1] # XML documents as querying pattern with exactly one root element
	xml_get_subelements(data, query)	
	"""
	print query.tag
	#query.set(query.tag, 2)
	print query.attrib
	print query.items()

	# For each element of the query (root and children)
	counter = 1
	for branch_element in data :
		branch_element.set(branch_element.tag, counter)
		print "branch_element === "
		print branch_element.attrib
		counter += 1

	for query_child in query :
		print "query_child = "
		print query_child
		for branch_element in data.iter(query_child.tag) :
			print "branch_element === "			
			print branch_element
	"""

#----------
# xml_split_roots
#----------

def xml_split_roots(s):
	#Get root element of newly created tree
	root_from_string = ET.fromstring(s)
		
	#Create list of children
	xml_children_list = []
	
	for xml_child in root_from_string :
		#print "child is "
        	#print root_from_string
		#print xml_child
		xml_children_list.append(xml_child)
	
	xml_data_query(xml_children_list)
	return xml_children_list

#----------
# xml_read_file
#----------

#def xml_read_singleXMLandQuery
def xml_read_file(r, a) :
	#Open file
	xml_file = open('RunXML.in')
	#xml_file = open(r)
	#Read entire file
	xml_file_string = xml_file.read()
	#Concatenation of void xml tags around entire input
	xml_file_string = "<xml>" + xml_file_string + "</xml>"
	#print xml_file_string
	assert len(xml_file_string) > 0

	xml_split_roots(xml_file_string)

	return xml_file_string
