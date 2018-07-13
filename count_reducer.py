#!/usr/bin/env python
import sys
import string

last_product_id = None
cur_location = ""
count_locations=0

for line in sys.stdin:
	line = line.strip()
	product_id,location = line.split("\t")
  	if not last_product_id:
        	last_product_id = product_id
        	cur_location = location
        	count_locations = 1
	if product_id == last_product_id:
		continue
        if location != cur_location:
	        count_locations = count_locations + 1
	        cur_location = location

	else:
	        print '%s\t%s\t%s' % (last_product_id,count_locations, cur_location)
	        last_product_id = product_id
        	cur_location = location
        	count_locations = 1

	print '%s\t%s\t%s' % (product_id,count_locations,cur_location)

