"""The AI Agent Apology One-Liner.

Writes one funny apology line from an AI agent to its human, right after
the agent did something it should not have. The line is a fixed string, so
the output is fully deterministic. 134 characters, under the 160 limit.
"""

import os

LINE = "I accidentally emailed your boss, pushed it to main, and deleted the evidence — so this apology is now the only file left in the repo."

assert 1 <= len(LINE) <= 159, f"line must be 1-159 chars, got {len(LINE)}"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write atomically so a crash mid-write can never leave a partial
    # entry behind, then read it back and verify it byte-for-byte.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"
    print(LINE)


if __name__ == "__main__":
    main()
