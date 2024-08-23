## Get VPC_ID
```shell
aws ec2 describe-vpcs \
--filters "Name=tag:Name,Values=nacl-example-myy" \
--query "Vpcs[0].VpcId" \
 --output text
```

## NACL (change the vpc id value)
```shell
aws ec2 create-network-acl \
--vpc-id vpc-008af8abf848f0c2c 
```

## Add entry
```shell
aws ec2 create-network-acl-entry \
--network-acl-id acl-00e239a9c972e1a1f \
--ingress \
--rule-number 90 \
--protocol -1 \
--port-range From=0,To=65535 \
--cidr-block 23.240.215.75/32 \
--rule-action deny
```

## Get AMI for Amazon Linux 2
### Grab the ImageId 
```shell
aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
--query "Images[?starts_with(Name, 'amzn2')]|sort_by(@, &CreationDate)[-1].ImageId" \
--region "us-west-1" \
--output text
```

### Update the ImageID parameter in template.yaml