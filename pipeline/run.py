from .ingest import ingest
from .transform import transform
import os

SOURCE_URL = "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/dev/.github/scripts/listings.json"

try:
    aws_reg = os.environ["AWS_REGION"]
    s3_bucket = os.environ["S3_BUCKET"]
    supabase_url = os.environ["SUPABASE_URL"]
except KeyError as error:
    raise KeyError(f"Missing required environment variable: {error}") from error

def run(source: str, postgres: str)->None:
    """
    Run the whole data pipeline
    """
    s3_key = ingest(source, aws_reg, s3_bucket)
    transform(postgres, s3_key)
    
    

if __name__ == "__main__":
    run(SOURCE_URL, supabase_url)