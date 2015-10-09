#!/bin/bash
COMMANDS=( 'python' 'fab' 'git' )
COMMANDSPACKAGES=( 'python' 'fabric' 'git')
comNum=${#COMMANDS[@]}
for(( i=0;i<$comNum;i++)); do
    echo "Checking if command \"${COMMANDS[${i}]}\" exists! It's package name is ${COMMANDSPACKAGES[${i}]}"
    if [ -z `which ${COMMANDS[${i}]}` ]  #if com empty
    then
        echo "${COMMANDS[${i}]} doesn't exist!"
        apt-get install ${COMMANDSPACKAGES[${i}]}
    else
        echo "${COMMANDS[${i}]} exists!"
    fi
    echo "Done!"
 done
