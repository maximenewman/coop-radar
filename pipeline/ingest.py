from typing import List
import requests
from datetime import date
import boto3
import json

def ingest(source: str, aws_reg: str, s3_bucket: str)->str:
    """
    Ingest data from APIs of job boards, or scraped public repos. 
    Then writes raw json to S3
    """
    today = date.today().isoformat()
    key = f"raw/{today}/listings.json"
    client = boto3.client("s3", region_name=aws_reg)

    raw_data = requests.get(source)
    raw_data.raise_for_status()

    client.put_object(Bucket=s3_bucket, Key=key, Body=raw_data.content, ContentType="application/json")

    print(f"Rows Pulled: {len(json.loads(raw_data.content))} + s3_key: {key}")

    return key


