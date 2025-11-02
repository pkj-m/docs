# Troubleshooting

405 Method Not Allowed
- Ensure you are using HTTPS, not HTTP.
- Default base: `https://api.getnivara.com`.

401 Unauthorized
- API key missing/invalid. Export `NIVARA_API_KEY=ak_live_...`.

Queue is full
- `emit(...)` returned `{ "status": "error", "error": "queue full" }`.
- Call `flush()`, increase `queue_size` via `configure(...)`, or use sync `record(...)` temporarily.

429 / 5xx
- Enable retries and backoff: `configure(retries=2)`.

ModuleNotFoundError: nivara
- Run `python3 -m pip install nivara`.

Connection refused / timeout
- Verify `NIVARA_BASE_URL` is reachable and correct.
- Try a quick `curl`:
  - `curl -i -X POST 'https://api.getnivara.com/v1/record' -H 'Content-Type: application/json' -H "X-API-Key: $NIVARA_API_KEY" -d '{"metric":"llm.request"}'`

