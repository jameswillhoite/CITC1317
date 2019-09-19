#!/bin/bash
##########################
##	Lab 4		##
## James Willhoite 	##
## 9/18/19		##
##########################
# Write HTML file from a csv file

HTML="<html><head><title>Lab 4 Willhoite</title><style>tr.TN{background-color: red;}</style></head><body><table border=\"1\">"

FILENAME="${1}"

# 1st add a <tr><td> to the begining of the 1st line
# 2nd replace all "," only on the first line with </td><td>
# 3rd Add a </td></tr> at the end of the first line
# 4th Add a <tr><td> at the beginning of each line that starts with a '"'
# 5th Replace all '","' with </td><td>
# 6th Replace the last '"' on each line with </td></tr> 
# 7th look for <td>TN</td> and replace the beginning <tr> with <tr class="TN"> to highlight the row red

INPUT_STREAM=`cat "${FILENAME}" | sed -E -e '1 s/^/\<tr\>\<td\>/' -e '1 s/\,/\<\/td\>\<td\>/g' -e '1 s/$/\<\/td\>\<\/tr\>/' -e 's/^\"/\<tr\>\<td\>/g'  -e 's/\"\,\"/\<\/td\>\<td\>/g' -e 's/\"$/\<\/td\>\<\/tr\>/g' -e '/\<td\>TN\<\/td\>/ { s/^\<tr\>/\<tr class\=\"TN\"\>/; }'`

echo $HTML
echo $INPUT_STREAM
echo "</table></body></html>"

