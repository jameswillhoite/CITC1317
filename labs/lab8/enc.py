#!/usr/bin/python

from sys import argv
import io as io
import os as os
from random import randint

file_path = ""
if len(argv[1]) == 0:
    print "Usage: ", argv[0], " <file>"
    exit(1)
else:
    file_path = argv[1]


encrypt_file = "encrypted_" + os.path.basename(file_path)

cypher = {}


# Generate a random cypher from the ASCII table
for i in range(32, 127):
    while True:
        val = chr(randint(32, 126))
        if val not in cypher.values():
            break

    cypher[chr(i)] = val

# Check to see if the file exists
try:
    f = io.open(file_path, "r")
    if not f.readable():
        print file_path + " is not readable"
        exit(1)

    # write a encryption file
    ec = open(encrypt_file, "w+")

    for line in f.readlines():
        ln = list(line.decode('utf-8'))
        for l in ln:
            cy = cypher.get(l)
            # If there is no cy then keep the l
            if not cy:
                cy = l
            ec.write(cy)

    ec.close()

    # write the cypher
    ef = open("cypher", "w")
    for key, val in cypher.items():
        ef.write(key+"::"+val+"|||")
    ef.close()



except IOError:
    print "Could not open the file"
    exit(1)

