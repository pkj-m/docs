"""Background emit with flush and stats.

export NIVARA_API_KEY=ak_live_...
"""

import nivara as nv


def main() -> int:
    nv.configure(timeout=2.0, retries=1, mode="background")
    print(nv.emit(metric="llm.request", input_tokens=10, output_tokens=2))
    print("flushed:", nv.flush(timeout=2.0))
    print("stats:", nv.stats())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
