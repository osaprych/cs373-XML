#!/usr/bin/env python

# -------
# imports
# -------

import sys
import random

# ----
# main
# ----



def gen_rand_data (size_data, query) :
	data = ""
	while size_data :
		data_and_dataclose = gen_rand_pair()
		if random.randint(1, 100) % 2 == 0 :
			data = data_and_dataclose[0] + query + data + data_and_dataclose[1]
		elif random.randint(1, 100) % 2 == 0 :
			data = data + data_and_dataclose[0] + data_and_dataclose[1]
		else :
			data = data + query + data_and_dataclose[0] + data_and_dataclose[1]
		size_data -= 1
	data_and_dataclose = gen_rand_pair()
	data = data_and_dataclose[0] + data + data_and_dataclose[1]
	return data


def gen_rand_query(size) :
	query = ""	
	while size :
		i_and_j = gen_rand_pair()
		if random.randint(1, 100) % 2 == 0 :
			query = i_and_j[0] + query + i_and_j[1]
		else :
			query = query + i_and_j[0] + i_and_j[1]
		size -= 1
	i_and_j = gen_rand_pair()
	query = i_and_j[0] + query + i_and_j[1]
	#print "random query generated",
	#print query
	#print ""
	return query
	
def gen_rand_pair() :
	s = get_rand_tag()
	i_and_j = []
	i_and_j.append("<" + s + ">")
	i_and_j.append("</" + s + ">")
	#print i_and_j
	return i_and_j

def get_rand_tag() :
	r = open('seuss.in')	
	s = r.readline()
	l = s.split()
	random_tag = []
	#rand_int = random.randint(0, len(l))
	#for i in xrange(0, number_of_tags) :
	random_tag = (l[random.randint(0, len(l) - 1)])
	#print l
	#print random_tag
	return random_tag

def acceptance() :
	i = 0
	while i < 1000 :
		gen_query = gen_rand_query(random.randint(1, 10))
		gen_data = gen_rand_data(random.randint(10,50), gen_query)
		print gen_data
		print gen_query
		print ""
		i += 1
	

acceptance()
