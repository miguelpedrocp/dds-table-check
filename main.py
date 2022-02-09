# this is your main.py file which acts as a control script
# this file should be reasonably lightweight and should contain calls to other files which contains methods, SQL scripts,
# python scripts etc

# this is an example of how you can create you own main.py
import config


import logging 
import os

logger=logging.getLogger(__name__)

# import external libraries
from dds_internal_tools.utils import utils_helper
from dds_internal_tools.aws import s3_helper
import boto3



def upload_logs_on_s3():
    try:
        logger.info('START')

        # establish connection with S3
        session = boto3.session.Session(
            aws_access_key_id=os.environ['AccessKeyID'],
            aws_secret_access_key=os.environ['SecretAccessKey'],
            aws_session_token=os.environ['SessionToken']
            )
        bucket_name=os.getenv('BUCKET_NAME')              

        # connect to S3
        s3io = s3_helper.S3Helper(session, bucket_name)

        logger.info('log_name: {}'.format(config.logging_helper_obj.log_name))

        s3io.upload_obj_to_s3(config.logging_helper_obj.log_stringio.getvalue(),config.logging_helper_obj.path_log_file)  
        logger.info("LOG data uploaded")        


        logger.info('SUCCESS')

    except Exception as err:
        logger.exception(err)


def main():
    try:
        logger.info('START')



        logger.info('SUCCESS')
      

    except Exception as err:
        logger.exception(err)

    finally:
        logger.info('FINAL')

        # upload logs on s3
        upload_logs_on_s3()




if __name__=='__main__':
    main()
