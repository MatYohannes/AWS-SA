from s3.sdk.python.s3 import *


def main():
    show_menus()
    operation = int(input("User selection: "))

    if operation == 1:
        bucket_name = input("bucket_name: ")
    region = 'us-west-1'

    if operation == 1:
        success = create_bucket(bucket_name, region)
        if success:
            print(f"Bucket '{bucket_name} created successfully in region '{region}")
        else:
            print(f"Failed to create bucket '{bucket_name}'")
    elif operation == 2:
        buckets = list_buckets()
        print('Existing buckets:')
        for bucket in buckets:
            print(bucket)
    elif operation == 4:
        bucket_name_del = input('Bucket to delete from: ')
        filename_del = input('Filename to delete: ')
        success_deletion = delete_object(bucket_name_del, filename_del)
        if success_deletion:
            print('Deletion successful.')
        else:
            print('Deletion failed.')
    elif operation == 3:
        file_path = input("Provide file path to upload: ")
        new_name = input("File name to upload or leave blank to keep existing name: ")
        if new_name == "":
            new_name = None

        upload_file(file_path, 'my-python-bucket-myy', new_name)
    elif operation == 5:
        bucket_del = input("Bucket to delete:")
        success_deletion = delete_bucket(bucket_del)
        if success_deletion:
            print(f"Deleted '{bucket_del}'")
        else:
            print(f"Failed to delete '{bucket_del}'")
    elif operation == 6:
        print("Exiting...")
        return False
    else:
        print("Invalid operation. use 'create' or 'list'")


if __name__ == '__main__':
    main()

