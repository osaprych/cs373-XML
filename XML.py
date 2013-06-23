#!/usr/bin/env python
import xml.etree.ElementTree as ET


id_counter = [1]
query_counter = [0]	



#----
# xml_output
#----

#extract first element of list

#sort list


#-----
# query_check (recursive)
#-----

def query_check(data_root, query_root):
	#Loop over query branch elements
	for query_child in query_root :
		print "searching new branch for :"
		print query_child
		print ""
		#if there are no query_children under a root
			#query_counter[0] += 1

		#Loop over data branch looking for remainder of query
		for data_child in data_root :
			if data_child.tag == query_child.tag :
				#recurse down tree to find next query el
				print "found query: "
				print query_child
				#print "at data element"
				#print data_child
				print "----"
				query_counter[0] += 1
				print "query_counter"
				print query_counter
				print "calling recurse with"
				print data_child
				print query_child
				query_check(data_child, query_child)
			else :
				#look for query in grandchildren
				query_check(data_child, query_root)
			
				

#----------
# depth_search (recursive)
#----------

def depth_search(parent, query_root) :
	#Outermost loop that tags IDs to elements of data tree
	for child in parent :
		#Assign ID to:element
		child.set(child.tag, id_counter[0])
		id_counter[0] += 1

		# PRINT CHILDREN WITH ID
		print ""
		print "Child ID dict entry:"
		print child.attrib	
	
		#Check for beginning of query pattern
		#*****Query Kickoff*****
		if (child.tag == query_root.tag) :
			print "Kicked off query_check!!!!!!!!!!!"
			query_check(child, query_root)		

		depth_search (child, query_root)


#----------
# xml_get_subelements
#----------

def xml_get_subelements(d, q) :
	d.set(d.tag, id_counter[0])
	id_counter[0] += 1
	#parse subtree
	depth_search(d,q)

#----------
# xml_data_query
#----------

def xml_data_query(xml_list) :
	data = xml_list[0] # XML documents with exactly one root element 
	query = xml_list[1] # XML documents as querying pattern with exactly one root element
	

	xml_get_subelements(data, query)

	return query



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
