#!/usr/bin/python

from sys import argv
import os as os

# get the cypher
cypher_file = argv[2]
cypher = {}

try:
    cf = open(cypher_file, "r")
    for l in cf.readlines():
        # build the cypher
        for key_val in l.split('|||'):
            temp = key_val.split("::")
            if len(temp) == 2:
                cypher[temp[1]] = temp[0]

    cf.close()


except IOError:
    print("Could not open the cypher")
    exit(1)

# get the encrypted file
enc_file = argv[1]

decrypt_file = "unencrypted_" + os.path.basename(enc_file)

try:
    ef = open(enc_file, "r")
    df = open(decrypt_file, "w+")

    for line in ef.readlines():
        ln = list(line)
        for ch in ln:
            cy = cypher.get(ch)
            if not cy:
                cy = ch
            df.write(cy)

    df.close()
    ef.close()


except IOError:
    print("Could not open the Encrypted file")
    exit(1)
