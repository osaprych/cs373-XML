#!/usr/bin/env python

# -------
# imports
# -------

import sys
import random

# ----
# main
# ----

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
	print query
	return query
	
def gen_rand_pair() :
	s = get_rand_tag()
	i_and_j = []
	i_and_j.append("<" + s + ">")
	i_and_j.append("</" + s + ">")
	print i_and_j
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
	r = 'RunXML.in'
	#gen_rand_query()

acceptance()
gen_rand_pair()
gen_rand_query(random.randint(1, 10))
