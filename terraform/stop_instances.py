import boto3

# Boto Connection
ec2 = boto3.resource('ec2', 'eu-west-2')

def lambda_handler(event, context):
  # Filters
  filters = [
    {
      'Name': 'instance-state-name', 
      'Values': ['running']
    }
  ]

  # Filter running instances that should stop
  instances = ec2.instances.filter(Filters=filters)

  # Retrieve instance IDs
  instance_ids = [instance.id for instance in instances]

  # stopping instances
stopping_instances = ec2.instances.filter(InstanceIds=instance_ids).stop()