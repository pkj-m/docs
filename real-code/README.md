# Nivara Python SDK — Developer Docs

Welcome to the developer documentation for the Nivara Python SDK.

- Audience: Python developers who want to record LLM/AI usage metrics.
- Package: `nivara`
- Default API base: `https://api.getnivara.com`

Quick links
- Getting Started: getting-started.md
- Installation: installation.md
- Configuration: configuration.md
- API Reference: api.md
- Concepts: concepts.md
- Troubleshooting: troubleshooting.md
- FAQ: faq.md
- Examples (code): examples/

If you’re just here to install and send a metric:

```
python3 -m pip install nivara
export NIVARA_API_KEY=ak_live_...
python - << 'PY'
import nivara
print(nivara.record(metric='llm.request', input_tokens=1, output_tokens=1))
PY
```

