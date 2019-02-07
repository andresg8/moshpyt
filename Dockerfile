#*******************************************************************************
#Dockerfile
#*******************************************************************************

#Purpose:
#This file describes the operating system prerequisites for MOSHPyT, and is used
#by the Docker software.
#Author:
#Cedric H. David, 2019-2019


#*******************************************************************************
#Usage
#*******************************************************************************
#docker build -t moshpyt:myimage -f Dockerfile .         #Create image
#docker run --rm --name moshpyt_mycontainer     \
#           -it moshpyt:myimage                          #Run image in container
#docker run --rm --name moshpyt_mycontainer     \
#           -v $PWD/input:/home/moshpyt/input   \
#           -v $PWD/output:/home/moshpyt/output \
#           -it moshpyt:myimage                          #Run and map volumes
#docker save -o moshpyt_myimage.tar moshpyt:myimage      #Save a copy of image
#docker load -i moshpyt_myimage.tar                      #Load a saved image


#*******************************************************************************
#Operating System
#*******************************************************************************
FROM debian:stable-slim


#*******************************************************************************
#Copy files into Docker image (this ignores the files listed in .dockerignore)
#*******************************************************************************
WORKDIR /home/moshpyt/
COPY . . 


#*******************************************************************************
#Operating System Requirements
#*******************************************************************************
RUN  apt-get update && \
     apt-get install -y --no-install-recommends $(grep -v -E '(^#|^$)' requirements.apt) && \
     rm -rf /var/lib/apt/lists/*


#*******************************************************************************
#Python requirements
#*******************************************************************************
ADD https://bootstrap.pypa.io/get-pip.py .
RUN python get-pip.py `grep 'pip==' requirements.pip` --no-cache-dir && \
    rm get-pip.py

RUN pip install --no-cache-dir -r requirements.pip


#*******************************************************************************
#Intended (default) command at execution of image (not used during build)
#*******************************************************************************
CMD  /bin/bash


#*******************************************************************************
#End
#*******************************************************************************
