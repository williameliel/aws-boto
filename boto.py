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
  #rsync -rave "ssh -i /Users/Williamgarcia/.ssh/aws1.pem" ubuntu@52.33.127.143:/var/www/vhost2/rainbowroom/dev/web/content/uploads /Users/Williamgarcia/websites/rainbowroom/web/content

