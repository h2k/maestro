# import pandas as pd
import os
import os.path
import subprocess
import zipfile
#import hashlib
import boto3

if __name__ == '__main__': 
    try:
        MainFileName = os.getenv('MainFileName')
        SourceBucket = os.getenv('SourceBucket')
        ProjectName = os.getenv('ProjectName')
        S3Key = os.getenv('S3Key')

        print("asb-long-post-ELTexecuter executed")
        
        if len(S3Key.split("/") ) >0 :
            S3Key = "/".join([ProjectName,S3Key])
        tempFilename = S3Key.split("/")[-1]

        # Download code file from S3
        s3Client = boto3.client("s3")
        downloadedFile  = s3Client.download_file(Bucket=SourceBucket, Key=S3Key, Filename=tempFilename)
        s3md5file = s3Client.head_object(Bucket=SourceBucket, Key=S3Key)['ETag'][1:-1]
        
        #print("before hashlib")
         
        #downloadedfile = hashlib.md5(open(tempFilename,'rb').read()).hexdigest()
        #if s3md5file  != downloadedfile:
        #    raise Exception("Unable to read Download code file from S3... Make sure the code is there")

        print("before unzipping")
        
        commands = []
        if tempFilename.split(".")[-1] == "zip":
            # path_to_zip_file = "file.zip"
            path_to_zip_file = tempFilename
            directory_to_extract_to = "".join(path_to_zip_file.split(".")[:-1])
            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
                if os.path.exists("requirements.txt") == True:
                    commands.append("pip install -r requirements.txt")
        elif tempFilename.split(".")[-1] == "py": 
            print("it is a python file !!!")
        else:
            raise Exception("Unable to read task configuration from dynamodb... task been condifured in there")
    
        print("before shell command execution")
        # excute shell command              
        cmd = "python "+ MainFileName
        commands.append(cmd)
        returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
        print('returned value:', returned_value)
        if returned_value == 0:
            print("Success")
        else:
            raise Exception("Error in excuting task in S3Key: "+S3Key)

    except Exception as e:
        print('Encountered Exception')
        print(e)
        responseVariables = {"ResponseCode":"-1","ResponseMessage":"Exception caught:" + str(e)}