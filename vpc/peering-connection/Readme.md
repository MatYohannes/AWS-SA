## Create two VPCs to connect first

# Create vpc peering connection
## Insert VPC ids
```shell
aws ec2 create-vpc-peering-connection --vpc-id vpc-0bb8a48f9e774dfa7 --peer-vpc-id vpc-04acf41ee67ba284b
```

## Accept vpc connection
```shell
aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id pcx-08972ffc477c3ef40
```

## Update Route Tables
### Input RT value (a) and destination cidr-block (b) and vpc-peering-connection id
```shell
aws ec2 create-route --route-table rtb-050902e9e2c1688f1 --destination-cidr-block 12.0.0.0/16 --vpc-peering-connection pcx-08972ffc477c3ef40
```

## Repeat previous step for the other RT
### Change the RT value and the destination-cidr-block
```shell
aws ec2 create-route --route-table rtb-0d30233b8c9ba84ae --destination-cidr-block 10.0.0.0/16 --vpc-peering-connection pcx-08972ffc477c3ef40
```

## Create yaml files for each (can use nacl yaml file)
### Create stacks with the yaml files

## Go to EC2 instance and connect to EC2-a session manager
### Change role in the session manager with:
```shell
sudo su - ec2-user
```
## Display html in session manager
```shell
wget -O - <IP address>
```

## Clean up
Delete the EC2 instance first
Then the peering connection along with the route tables
Finally, delete the VPCs then stacks

## Clean up
Delete the EC2 instance firstThen the peering connection along with the route tablesFinally, delete the VPCs## Clean upDelete the EC2 instance firstThen the peering connection along with the route tablesFinally, delete the VPCs
