## Create a new s3 bucket

```commandline
aws s3 mb s3://checksums-example-myy
```

## Create a file for checksum test

```commandline
echo "Hello Earth" > myfile.txt
```

## Get a checksum of a file for md5

```md
md5sum myfile.txt
# 4f5855a17500f758421000f8361ec3bf  myfile.txt
```

## Upload file to s3
```
aws s3 cp myfile.txt s3://checksums-example-myy
aws s3api head-object --bucket checksums-example-myy --key myfile.txt
```
## upload a file with a different kind of checksum

```shell
sudo apt-get install rhash -y
rhash --crc32 --simple myfile.txt
```

```shell
aws s3api put object \
--bucket="checksums-example-myy" \
--key="myfilesha1.txt" \
--body="myfile.txt" \
--checksum-algorithm="sha1" \
--checksum-sha1="c726204e4dc9589affe81e59260019d31ae5d5db" 
```

# value from rhash command above