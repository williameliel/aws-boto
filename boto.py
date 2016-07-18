#import required modules
import boto3
import os

#create a boto ec2 client
client = boto3.client('ec2')

#get all instances that are tagged under the sbe-auto-group
response = client.describe_instances(
  Filters=[
        {
            'Name': 'tag-key',
            'Values': [
                        'aws:autoscaling:groupName'
                      ],
            'Name': 'tag-value',
            'Values': [
                        'sbe-auto-group'
                      ]
           
        },
    ]
)


destination = '/var/www/vhosts'
source = destination  + '/sbe.com'

for reservations in response['Reservations']:
  for instance in reservations['Instances']:
    if(instance['State']['Name']=="running"):
      privateIp = instance['PrivateIpAddress']
      publicIp = instance['PublicIpAddress']
      #print(publicIp)
      os.system("rsync --exclude-from exclude.txt -rave 'ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null  -i /home/ubuntu/.ssh/aws1.pem' " + source + ' ' +  'ubuntu@' + publicIp + ':' + destination )

