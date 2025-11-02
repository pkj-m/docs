"""OpenAI one-liner ➜ Nivara emit.

Prereqs:
  export OPENAI_API_KEY=sk-...
  export NIVARA_API_KEY=ak_live_...

pip install: openai, nivara
"""

from openai import OpenAI
import nivara as nv


def main() -> int:
    client = OpenAI()
    resp = client.responses.create(model="gpt-4o-mini", input="hello")
    print(nv.emit(metric="llm.request", **nv.from_openai(resp)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
