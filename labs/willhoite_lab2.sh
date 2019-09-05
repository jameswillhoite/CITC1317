#!/bin/bash

#get list of files in directory as array
DIR=(`find ./ -type f`)

#variables
BYTES=0
TOTAL_FILES=0
TOTAL_WRITABLE=0
TOTAL_READABLE=0
TOTAL_EXECUTABLE=0


#Loop Though and add up file size
for file in "${DIR[@]}"
do
	#get the size of the file | trim any leading whitspace | cut the line at the space and return the first one
	TEMP=`wc -c "${file}" | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f1`
	let BYTES+=TEMP

	let TOTAL_FILES++

	if [[ -r "${file}" ]]; then
		let TOTAL_READABLE++
	fi

	if [[ -w "${file}" ]]; then
		let TOTAL_WRITABLE++
	fi

	if [[ -x "${file}" ]]; then
		let TOTAL_EXECUTABLE++
	fi
done

#Get the total number of files with #!/bin/ at the beginning
TOTAL_SCRIPT=(`grep "^\#\!\/bin\/" ./*`)


printf  "Total Bytes in Current Directory			 : $BYTES (~%.0fKB) \n" $((BYTES / 1000))
echo -e "Total Files in Current Directory			 : $TOTAL_FILES"
echo -e "Total Files Readable		      			 : $TOTAL_READABLE"
echo -e "Total Files Writable					 : $TOTAL_WRITABLE"
echo -e "Total File Executable					 : $TOTAL_EXECUTABLE"
echo -e "Estimated number of shell script files in this directory : ${#TOTAL_SCRIPT[@]}"
