# Set the base image
FROM python:2.7

# File Author / Maintainer
MAINTAINER bjg

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Copy the application folder inside the container
ADD /sqs_application /sqs_application

# Get pip to download and install requirements:
RUN pip install -r /sqs_application/requirements.txt
RUN pip install boto


# Expose listener port
EXPOSE 5000
RUN mkdir /data

# Set the default directory where CMD will execute
WORKDIR /sqs_application
# Set the default command to execute    
# when creating a new container
CMD python server.py
