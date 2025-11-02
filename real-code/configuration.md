# Configuration

Environment variables
- `NIVARA_API_KEY` (required)
- `NIVARA_BASE_URL` (optional, default `https://api.getnivara.com`)
- Optional tuning:
  - `NIVARA_TIMEOUT` (default `2.0` seconds)
  - `NIVARA_RETRIES` (default `0`)
  - `NIVARA_MODE` (`background` | `sync`, default `background`)
  - `NIVARA_QUEUE_SIZE` (default `10000`)
  - `NIVARA_DEBUG` (`1` to enable basic debug prints)

Programmatic configuration
```python
import nivara as nv

nv.configure(
  timeout=2.0,
  retries=2,
  mode='background',
  queue_size=10000,
  debug=False,
)
```

Defaults
- If you don’t call `configure(...)`, the SDK reads env values (above) and starts in background mode when first used.
- The global client can be reconfigured at any time; changing `mode` restarts/stops the worker.
