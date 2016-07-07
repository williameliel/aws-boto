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
                        'group-xyz'
                      ],
        },
    ]
)

destination = '/var/www/vhosts'
source = destination  + '/foo.com' # /var/www/vhosts/foo.com

for instance in response['Reservations'][0]['Instances']:
  privateIp = instance['PrivateIpAddress'] # depending on your environment you can use either public or private address
  publicIp = instance['PublicIpAddress'] 
  
  os.system("rsync -rave 'ssh -i /home/ubuntu/.ssh/aws1.pem' " + source + ' ' +  'ubuntu@' + publicIp + ':' + destination )
