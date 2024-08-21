## Create a bucket
```shell
aws s3 mb s3://encrypt-client-myy
```

## Create a Key Using OpenSSL
```shell
export CLIENT_ENCRYPT_S3=$(openssl rand -base64 32)
```

## Create a file
```shell
echo "Hello bees" > hello.txt
```