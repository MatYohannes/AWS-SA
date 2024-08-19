## Create a bucket
```shell
aws s3 mb s3://change-storage-myy
```

## Create a file
```shell
echo "Hello World" > hello.txt
```

aws s3 cp hello.txt s3://change-storage-myy --storage-class STANDARD_IA