## Convert yaml file to json

The command
```shell
yq -o json policy.yaml > policy.json
```

The bash script

```shell
./updateYamlToJson
```

Create IAM Policy
```shell
aws iam create-policy \
--policy-name my-fun-policy \
--policy-document file://policy.json
```

## Attach policy to user
```shell
aws iam attach-user-policy \
--policy-arn arn:aws:iam::014498645771:policy/my-fun-policy \
--user-name matyohannes
```