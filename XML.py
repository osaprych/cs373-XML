#!/usr/bin/env python
import xml.etree.ElementTree as ET
import sys

"""
This program parses XML data query pairs to find the number of times and where query appears in data.
"""

id_counter = [1]
query_counter = [0]	
catch_id = []
query_check_false = True


def reset_globals() :
	"""
	Start clean counter for new incoming data query pair.
	"""
	global id_counter
	global query_counter
	global catch_id
	id_counter = [1]
	query_counter = [0]
	catch_id = []


#----
# xml_output
#----

def xml_output() :
	"""
	Prints num occurances to first line of output and ID num of element that occurs the query pattern
	"""
	#Print num occurances to first line of output
	print query_counter[0]
	#ID num of element that occurs the query pattern
	for element in catch_id :	
		print element
	print ""
	reset_globals()
	assert id_counter == [1]
	assert query_counter == [0]
	assert catch_id == []
	return query_counter[0]

					
#-----
# xml_query_check (recursive)
#-----

def xml_query_check(data, query_root):
	"""
	Depth First Search through query to find matching data elements and ensure that the entire query is present
	"""
	#Loop over query branch elements
	for query_child in query_root :
	            #Capture list returned by findall of all subelements of data
	            d_s_l = data.findall(query_child.tag)
	            
	            #Query ele was not found in data children
	            if len(d_s_l) == 0:
		            global query_check_false
		            query_check_false = False

	
	            #Else this particular query ele was found in data
	            else :
			assert len(d_s_l) > 0
			#Check next layer of data subelements
			for dsl_ele in d_s_l :
				xml_query_check(dsl_ele, query_child)

	return "checked_query"
		                 
		                        

#------
# xml_det_kickoff
#------

def xml_det_kickoff(data, query) :
	"""
	Check for beginning of query pattern as parse data, and if find query root check for the rest of query.
	"""
	#Check for beginning of query pattern as parse data
	if (data.tag == query.tag) :

		#If find query root check for the rest of query
		global query_check_false
		query_check_false = True
		xml_query_check(data, query)

		#If find complete query nested beneath data element
		if (query_check_false != False) :
			#Increment num complete queries found
			query_counter[0] += 1
			id_dict = data.attrib
			id_val = id_dict[data.tag]
			#Add kickoff id to list
			catch_id.append(id_val)
			assert len(catch_id) > 0
	return data



#----------
# xml_depth_search (recursive)
#----------

def xml_depth_search(parent, query_root) :
	"""
	Parse and label all the elements in the subtree beneath given data parent
	"""
	#Outermost loop that tags IDs to elements of data tree
	for child in parent :
		#Assign ID to:element
		child.set(child.tag, id_counter[0])
		id_counter[0] += 1	
		assert child.tag != None
		#Check for query in data
		xml_det_kickoff(child, query_root)

		xml_depth_search (child, query_root)
	return True 



#----------
# xml_get_subelements
#----------

def xml_get_subelements(d, q) :
	"""
	Assign ID to root of data, and check it against the query root. Call depth_search with root of data.
	When that returns, it's known that the entire data tree was parsed.
	At that point print output stored in global variables. 
	"""
	assert len(id_counter) > 0
	#Assign ID to root of data subtree
	d.set(d.tag, id_counter[0])
	id_counter[0] += 1

	#Check for query from root of data
	xml_det_kickoff(d, q)

	#parse the rest of the data subtree
	xml_depth_search(d,q)
	#When finished parsing data, output findings
	xml_output()
	return True

#----------
# xml_data_query
#----------

def xml_data_query(xml_list) :
	"""
	Iterate through data query pairs which may be multiple depending on the input file. 
	"""

	i = 0
	j = 1

	while j <= len(xml_list):
		 # XML documents with exactly one root element 
		data = xml_list[i]
		# XML documents as querying pattern with exactly one root element
		query = xml_list[j]
		#Iterate to next data/query child pair
		i += 2
		j += 2
		assert type(data) is ET.Element
		assert type(data) is ET.Element
		#Perform program function on the extracted
		#data/query xml pair
		xml_get_subelements(data, query)

	return query



#----------
# xml_split_roots
#----------

def xml_split_roots(s):
	"""
	Make list of data and query root elements that are found when parsing string as an element tree.
	"""
	#Get root element of newly created tree
	root_from_string = ET.fromstring(s)
		
	#Create list of children
	xml_children_list = []
	
	for xml_child in root_from_string :
		xml_children_list.append(xml_child)
	
	xml_data_query(xml_children_list)

	assert len(xml_children_list) > 0	

	return xml_children_list

#----------
# xml_read_file
#----------

def xml_read_file(r, a) :
	"""
	Reads given file into one string.
	"""
	sys.setrecursionlimit (1000000) 
	#Read entire file
	xml_file_string = r.read()
	#Concatenation of void xml tags around entire input
	xml_file_string = "<xml>" + xml_file_string + "</xml>"
	assert len(xml_file_string) > 0

	xml_split_roots(xml_file_string)

	return xml_file_string
