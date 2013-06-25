#!/usr/bin/env python
import xml.etree.ElementTree as ET


id_counter = [1]
query_counter = [0]	
catch_id = []


#----
# xml_output
#----

def xml_output() :
	print query_counter[0]
	for element in catch_id :	
		print element

#extract first element of list

#sort list

#-----
# query_search (recursive)
#-----

def query_search(data_root, query) :
	for data_child in data_root :
		if data_child.tag == query.tag :
			#recurse down tree to find next query element
			return True
		else :
			#look for query in grandchildren
			query_search(data_child, query)
	#Never found match to query element	
	return False


#-----
# query_check (recursive)
#-----

def query_check(data, query_root):
	#Loop over query branch elements
	for query_child in query_root :
		"""
		print "query_check() searching new branch for :",
		print query_child
		print ""
		"""
		#Returns a True for each query child found
		b1 = query_search(data, query_child)
		#If could not find query_child in parse of data xml, ret false 
		if b1 == False :
			return False

		#if there are no query_children under a root
			#query_counter[0] += 1
		#if query_child == None :
		#	raise EndOfQuery
		#Loop over data branch looking for remainder of query
	return True
			


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
		print "depth_search ID dict entry:"
		print child.attrib	
	
		#Check for beginning of query pattern
		#*****Query Kickoff*****
		if (child.tag == query_root.tag) :
			#print "Kicked off query_check!!!!!!!!!!!"
			

			b0 = query_check(child, query_root)
			#*******			
			if (b0) :
				print "*****query_check returned true to depth_search"
				query_counter[0] += 1
				print "child.attrib ",
				id_dict = child.attrib
				id_val = id_dict[child.tag]
				print id_val
				catch_id.append(id_val)

		depth_search (child, query_root)
	return True


#----------
# xml_get_subelements
#----------

def xml_get_subelements(d, q) :
	d.set(d.tag, id_counter[0])
	id_counter[0] += 1
	#parse subtree
	depth_search(d,q)
	xml_output()

#----------
# xml_data_query
#----------

def xml_data_query(xml_list) :
	data = xml_list[0] # XML documents with exactly one root element 
	query = xml_list[1] # XML documents as querying pattern with exactly one root element
	#print "PRINTING QUERY"
	#print 


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
	#xml_file = open('RunXML_altered2.in')
	#xml_file = open(r)
	#Read entire file
	xml_file_string = r.read()
	#Concatenation of void xml tags around entire input
	xml_file_string = "<xml>" + xml_file_string + "</xml>"
	#print xml_file_string
	assert len(xml_file_string) > 0

	xml_split_roots(xml_file_string)

	return xml_file_string
