"""
Basic script to download the XML file from internet fpr GDACS system
Used on AWS Lambda function
"""

import json
import boto3
from datetime import datetime
import requests
import urllib3

currentTime = datetime.now()
timestamp = str(currentTime.strftime("%Y%m%d%H%M"))
filename = f'GDACS_RAW.{timestamp}.xml'

s3 = boto3.client('s3')


def lambda_handler(event, context):
    url = "https://www.gdacs.org/xml/rss.xml"
    bucket = "atlas-watch-ingestfiles"
    folder = "gdacs"
    fullpath = f'{folder}/{filename}'

    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
 
    s3.upload_fileobj(response, bucket, fullpath)