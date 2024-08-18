# Contents
## s3 bash script
Parameters needed
- create-bucket: pass bash script with 1 argument (s3 bucket name)
- delete-bucket: pass bash script with 1 argument (s3 bucket name)
- delete-bucket: pass bash script with 1 argument (s3 Object Key)
- get-latest-bucket: None
- list-buckets: None
- list-objects: pash bash script with 1 argument (s3 bucket name)
- put-object: pash bash script with 2 arguments (s3 bucket name, filename prefix)
- sync: pash bash script with 2 arguments (s3 bucket name, filename prefix)

How to Set Environment Variables in Windows PowerShell:
In Windows PowerShell, you can set environment variables using the following syntax:

- powershell
    env AWS_CLI_AUTO_PROMPT="on-partial"
- bash
    export AWS_CLI_AUTO_PROMPT="on-partial"

To check if user is connected to aws:
aws sts get-caller-identity

#CLI Commands
aws s3api list-buckets --query 'Buckets[].Name' --ouput table (table or text)

## Creating S3 Bucket
line below is for terminal, creating new bucket called "my-new-bucket-myy"
./s3/bash-scripts/create-bucket my-new-bucket-myy

