## Create 2 buckets to preform a datasync

```shell
aws s3 mb s3://source-datasync-0901
aws s3 mb s3://dest-datasync-0901
```
## Upload file
```shell
echo "GUNDAM" > gundam.txt
aws s3 cp gundam.txt s3://source-datasync-0901
```

## Sync buckets
```shell
aws s3 sync s3://source-datasync-0901 s3://dest-datasync-0901
```