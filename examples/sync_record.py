"""Synchronous record.

export NIVARA_API_KEY=ak_live_...
"""

from datetime import datetime, timezone
import nivara as nv


def main() -> int:
    res = nv.record(
        metric="llm.request",
        ts=datetime.now(timezone.utc),
        input_tokens=5,
        output_tokens=1,
    )
    print(res)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
