#!/usr/bin/env sh -e

# This script will create a new base Alpine Docker container. Afterwards, it will
# run commands to create a layers directory, install specified package, and then
# zip them. Finally the zip is copied to the users specified directory. This is
# perfect for creating AWS Lambda layers

contName="mkzip"
imgName="personamsolis/layermaker"

if [ -z $1 ]; then
    echo -e "Please run the command with the following arguments:\n 
    createPythonLayer.sh [target_directory] [python_vers: 3.9, 3.8, 3.7] [package]"
    exit 385
fi

# start docker container
docker run --rm --name $contName $imgName

# Execute commands



# stop container (it will be auto removed)
docker stop $contName