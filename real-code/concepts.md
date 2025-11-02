# Concepts

Background vs. Sync
- Background (default): `emit(...)` enqueues to a worker thread.
  - Pros: non‑blocking, optional retries with backoff.
  - Cons: eventual delivery; inspect `stats()` for errors.
- Sync: `record(...)` sends immediately in the calling thread.
  - Pros: immediate result; great for CLIs/tests.
  - Cons: call can block; handle errors inline.

Queueing
- Bounded queue prevents unbounded memory growth.
- When full, `emit(...)` returns `{ "status": "error", "error": "queue full" }`.

Retries & Backoff
- Enable with `configure(retries>0)`; applies to 408, 429, and 5xx.
- Exponential backoff + light jitter.

Sampling
- Client‑side sampling via `emit(..., sample_rate=<0..1>)` to throttle volume.

Timestamps
- You can pass `ts` as a `datetime` or RFC3339 string.
- If omitted, the server assigns current UTC time.

