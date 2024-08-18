# AWS-SA
Solution Architect
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

