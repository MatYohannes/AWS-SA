## Create a bucket
```shell
aws s3 mb s3://encryption-example-myy
```

## Create a file and put object with encryption SSE-S3
```shell
echo "Hello Vulcan" > vulcan.txt
aws s3 cp vulcan.txt s3://encryption-example-myy
```

## Check if KMS keys exists
```shell
aws kms list-keys
```

## Put object with encryption with SSE-KMS
```shell
aws s3api put-object \
--bucket encryption-example-myy \
--key vulcan.txt \
--body vulcan.txt \
--server-side-encryption aws:kms \
--ssekms-key-id e92713d8-45ee-40d5-bdf9-9bea89e2fcd8
```

## Put object with SSE-C [Failed Attempt]
```shell
# Generate 32 random bytes of data for key
# base64 takes raw binary and encodes
# result is random string of char 44 len, use for key
export BASE64_ENCODED_KEY=$(openssl rand -base64 32)
echo $BASE64_ENCODED_KEY

export MD5_VALUE=$(echo $BASE64_ENCODED_KEY | md5sum | awk '{print $1}' | base64)
echo $MD5_VALUE

aws s3api put-object \
--bucket encryption-example-myy \
--key vulcan.txt \
--body vulcan.txt \
--sse-customer-algorithm AES256 \
--see-customer-key $BASE64_ENCODED_KEY \
--sse-customer-key-md5 $MD5_VALUE \
--sse-customer-md5 
```
## Put Object with SSE-C via AWS s3
```shell
openssl rand -out ssec.key 32

aws s3 cp vulcan.txt s3://encryption-example-myy/vulcan.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```
## Download the SSE-C encrypted file back
aws s3 cp s3://encryption-example-myy/vulcan.txt vulcan2.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
