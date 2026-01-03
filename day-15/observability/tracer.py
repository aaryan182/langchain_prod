import time
import uuid
from contextlib import contextmanager
from typing import Optional
from observability.logger import log_event


@contextmanager
def trace_span(name: str, metadata: Optional[dict] = None):
    trace_id = str(uuid.uuid4())
    start = time.time()
    
    log_event(
        "trace_start",
        {
            "trace_id": trace_id,
            "span": name,
            "metadata": metadata or {}
        }
    )
    
    try:
        yield trace_id
    except Exception as e: 
        log_event(
            "trace_error",
            {
                "trace_id": trace_id,
                "span": name,
                "error": str(e)
            }
        )
        raise
    finally:
        duration = time.time() - start
        log_event(
            "trace_end",
            {
                "trace_id": trace_id,
                "span": name,
                "duration_ms": int(duration * 1000)
            }
        )