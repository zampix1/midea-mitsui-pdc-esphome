import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATTERNS = [
    (re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"), "private 192.168 address"),
    (re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"), "private 10/8 address"),
    (
        re.compile(r"\b172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}\b"),
        "private 172.16/12 address",
    ),
    (re.compile(r"\b[0-9a-f]{2}(:[0-9a-f]{2}){5}\b", re.I), "MAC address"),
    (re.compile(r"C:\\Users\\[^\\\r\n]+", re.I), "Windows user profile path"),
    (re.compile(r"\\\\\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\"), "UNC IP path"),
    (re.compile(r"/home/[^\s/]+"), "Linux home path"),
]

ALLOWED_FILES = {
    Path("tests/static_privacy_check.py"),
}


def iter_public_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts:
            continue
        if rel in ALLOWED_FILES:
            continue
        yield rel, path


def main() -> int:
    failures = []
    for rel, path in iter_public_files():
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for pattern, label in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                failures.append(f"{rel}: {label}")
    if failures:
        print("\n".join(failures))
        return 1
    print("static privacy check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
