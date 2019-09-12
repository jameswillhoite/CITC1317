#!/bin/bash

###########
# James Willhoite
# 9/11/19
# Lab 3
##########

EMAIL=0
PHONE=0

printUsage() {
	printf "Usage: $0 (-e|-p) input_file\n"
}


# Loop through and get the command line variable "-"
while getopts ":e?p?" option; do
	case "$option" in
		e)
			EMAIL=1
			;;
		p)
			PHONE=1
			;;
		h)
			printUsage
			;;
		*)
			printf "Invalid Input\n"
			printUsage
			exit 1
			;;
	esac
done

# Test to see if any options were given
if [ $OPTIND -eq 1 ]; then
	printUsage
	exit 1
fi

shift # past the option

FILENAME=$@

# Test to make sure there is a file given
if [ -z "$FILENAME" ]; then
	printf "ERROR! No File Given\n"
	exit 1
fi

#Test to make sure the file exists
if [ ! -f "$FILENAME" ]; then
	printf "ERROR! File $FILENAME doesn't exist\n"
	exit 1
fi

if [ $EMAIL -eq 1 ]; then
	printf "Email Addresses\n\n"
	egrep -o -E '[a-zA-Z0-9\-\_\.]*\@[a-zA-Z0-9\-\_\.]*\.[a-zA-Z]*' "${FILENAME}"
	printf "\n\n"
fi

if [ $PHONE -eq 1 ]; then
	printf "Phone Numbers\n\n"
	egrep -o -w -E '([0-9]{3,3}\-[0-9]{3,3}\-[0-9]{4,4}|\([0-9]{3,3}\)\s?[0-9]{3,3}\-[0-9]{4,4})' "${FILENAME}"
	printf "\n\n"
fi


