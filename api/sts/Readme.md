## Create a user with no permission, then generate access keys
```shell
aws iam create-user --user-name sts-machine-user
aws iam create-access-key --user-name sts-machine-user --output table
```
### Save Access Key and Secret and insert to aws configure to change users
```shell
aws configure
```
### Test user change happened
```shell
aws sts get-caller-identity
```
## Create a Role

```shell
chmod u+x bin/deploy
./bin/deploy
```

## Clean up

```shell
aws iam delete-access-key \
--access-key-id #### \
--user-name sts-machine-user
aws iam delete-user --user-name sts-machine-user
```
