#!/usr/bin/env python
import sys
for line in sys.stdin:
    # Setting some defaults
	user_id = ""
	product_id = "-"
	location = "-"

	line = line.strip()
	splits = line.split(",")
	if len(splits) == 5: 
		user_id = splits[2]
		product_id = splits[1]
	elif len(splits) == 4:
		user_id = splits[0]
		location = splits[3]
	print '%s\t%s\t%s' % (user_id,product_id,location)
