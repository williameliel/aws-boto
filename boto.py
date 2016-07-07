import boto3
import sh
from sh import rsync

client = boto3.client('ec2')

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
                      ],
        },
    ]
)

#print(response['Reservations'][0]['Instances'])
for instance in response['Reservations'][0]['Instances']:
  privateIp= instance['PrivateIpAddress']
  publicIp = instance['PublicIpAddress']
  print(publicIp, privateIp)
  
