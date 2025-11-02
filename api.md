# API Reference

Top‑level functions

```
configure(*, base_url=None, api_key=None, timeout=2.0, retries=0, mode='background', queue_size=10000, debug=False) -> None
emit(*, metric, ts=None, user_identifier=None, input_tokens=None, output_tokens=None, cached_tokens=None, reasoning_tokens=None, timeout=None, sample_rate=1.0) -> dict
record(*, metric, ts=None, user_identifier=None, input_tokens=None, output_tokens=None, cached_tokens=None, reasoning_tokens=None, timeout=None) -> dict
set_user(user_identifier: str | None) -> None
from_openai(response, *, user_identifier=None) -> dict
flush(timeout: float | None = None) -> bool
close() -> None
stats() -> dict
```

Arguments
- `metric` (str, required): free‑form name, e.g., `"llm.request"`.
- `ts` (datetime or RFC3339 string): omit to let the server assign current UTC.
- `user_identifier` (str): client-supplied end‑user label.
- `input_tokens`, `output_tokens`, `cached_tokens`, `reasoning_tokens` (int ≥ 0).
- `timeout` (float): per‑request timeout.
- `sample_rate` (0..1): client‑side sampling (emit only).

Return values
- Success: `{"status":"ok","http_status":201}` (+ server JSON, if any)
- Enqueued: `{"status":"queued"}`
- Sampled out: `{"status":"sampled_out"}`
- Error: `{"status":"error","http_status":<int?>,"error":"..."}`

Notes
- Only supported fields are sent; unknown values are omitted.
- Datetime values are converted to RFC3339 (`Z` suffix, UTC).
- Retries (408/429/5xx) apply when configured via `configure(retries=...)`.

