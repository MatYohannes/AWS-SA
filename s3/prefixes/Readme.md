## Create a bucket
```shell
aws s3 mb s3://prefixies-try-myy
```

## Create a folder
# folder is created with --key="hello/" (the / makes it a folder)
```shell
aws s3api put-object --bucket="prefixies-try-myy" --key="hello/"
```