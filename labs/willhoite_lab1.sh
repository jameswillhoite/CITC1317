#!/bin/bash
clear
USER=`whoami`
echo "Hello World! This is $USER's first script."
echo "Quick summary of the current state:"
CUR_DIR=`pwd`
echo -e "1) Current Directory:\n $CUR_DIR\n"
CONT_DIR=`ls -la`
echo -e "2) Contents of current directory (including permissions):\n $CONT_DIR\n"
CUR_PROCESS=`ps`
echo -e "3) Processes currently running here:\n$CUR_PROCESS\n"
CUR_USERS=`w`
echo -e "4) Users currently logged on and their activity:\n$CUR_USERS\n"
