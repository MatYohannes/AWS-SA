## Create a bucket
```shell
aws s3 mb s3://cors-example-myy
```
## Change block public access
```shell
aws s3api put-public-access-block \
--bucket cors-example-myy \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```
## Create a bucket policy
```shell
aws s3api put-bucket-policy --bucket cors-example-myy --policy file://bucket-policy.json
```
## Turn on static website hosting
```shell
aws s3api put-bucket-website --bucket cors-example-myy --website-configuration file://website.json
```
## Upload index.html file and include a resource for cross-origin-resourcing
aws s3 cp index.html s3://cors-example-myy

## View website
http://cors-example-myy.s3-website.us-west-1.amazonaws.com
