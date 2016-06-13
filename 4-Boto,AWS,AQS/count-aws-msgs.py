import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import urllib2
import sys

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = ""
secret_access_key = ""
keypart1 = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read()
access_key_id, secret_access_key = keypart1.split(':')

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

q_name = sys.argv[1]

q = conn.get_queue(q_name)

msg_tot = q.count()

print ("> Messages in the queue: " + str(msg_tot))
