from .ingest import ingest
from .transform import transform
from typing import List

def run(sources: List[str], postgres: str)->None:
    """
    Run the whole data pipeline
    """
    ingest(sources)
    transform(postgres)
    
    

if __name__ == "__main__":
    run(["linkedin.com", "indeed.com"], "postgres+...")