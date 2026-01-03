import logging 
import json
import uuid
from datetime import datetime

logging.basicConfig(level= logging.INFO)
logger = logging.getLogger("LLM-system")

def log_event(event_type: str, payload: dict):
    """
    Structured logs for LLM systems.
    These logs are machine readable.
    """
    log_entry = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        **payload
    }
    
    logger.info(json.dumps(log_entry))
    
# Why structured logs:
# Queryable
# Indexable
# Works with ELK / Datadog / CloudWatch