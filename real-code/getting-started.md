# Getting Started

This guide shows how to install, configure, and send your first metric.

Requirements
- Python 3.8+
- A Nivara API key: `ak_live_<id>.<secret>`

Install
```
python3 -m pip install nivara
```

Environment
```
export NIVARA_API_KEY="ak_live_..."            # required
export NIVARA_BASE_URL="https://api.getnivara.com"  # optional (default)
```

Send your first metric (background emit)
```python
import nivara as nv

# Non‑blocking enqueue; server sets ts if omitted
nv.emit(metric='llm.request', user_identifier='user_42', input_tokens=120, output_tokens=30)
nv.flush(timeout=2.0)
print('stats:', nv.stats())
```

Synchronous one‑shot
```python
from datetime import datetime, timezone
import nivara as nv

print(nv.record(metric='llm.request', ts=datetime.now(timezone.utc), input_tokens=80, output_tokens=20))
```
