# /src/common/memory.py


import os

import psutil

_process = psutil.Process(os.getpid())


def log_memory(stage: str) -> None:
    rss_mb = _process.memory_info().rss / 1024 / 1024

    print(
        f"[MEMORY] {stage}: {rss_mb:.1f} MB"
    )