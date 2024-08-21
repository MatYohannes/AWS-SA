## Create a bucket

```shell
aws s3 mb s3://metadata-bucket-myy
```

### Create new file
```shell
echo "Hello Earth" > hello.txt
```

## Upload file with metadata
```shell
aws s3api put-object --bucket metadata-bucket-myy --key hello.txt --body hello.txt --metadata Planet=Earth
```

### Get Metadata from object
```shell
aws s3api head-object --bucket metadata-bucket-myy --key hello.txt
```
