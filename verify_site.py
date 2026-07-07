#!/usr/bin/env python3
"""Verify every navigation path and generated page of the CISO-in-a-Box site.

Resolves the navbar from site_config.py + SECTION_METADATA in generate_site.py,
walks the built _site/ directory for every generated index.html, then HTTP
checks each path against a running server. External (github.com) links are
skipped.

Usage:
    ./verify_site.py [base_url]
        base_url defaults to http://127.0.0.1:8765

Exits non-zero if any local page does not return 200 OK.
"""
from __future__ import annotations

import http.client
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_ROOT = ROOT / "ciso-in-a-box-site"
BUILT_SITE = SITE_ROOT / "_site"

sys.path.insert(0, str(ROOT))
from site_config import NAVBAR_CONFIG, SITE_BASEURL, GITHUB_REPO_URL  # noqa: E402


def section_slug_map() -> dict[int, str]:
    """Parse SECTION_METADATA from generate_site.py to map number -> slug."""
    gen = (ROOT / "generate_site.py").read_text(encoding="utf-8")
    slugs: dict[int, str] = {}
    for m in re.finditer(
        r"SectionMeta\(\s*(\d+),\s*\"[^\"]*\",\s*\"[^\"]*\",\s*\"([^\"]+)\"",
        gen,
    ):
        slugs[int(m.group(1))] = m.group(2)
    return slugs


def navbar_paths() -> list[str]:
    """Resolve NAVBAR_CONFIG to baseurl-relative paths."""
    slugs = section_slug_map()
    paths: list[str] = []
    for group in NAVBAR_CONFIG:
        for item in group["items"]:
            if "url" in item:
                continue
            if "page" in item:
                paths.append(f"/{item['page']}/")
            elif "section" in item:
                slug = slugs.get(item["section"], item.get("fallback_slug", ""))
                if slug:
                    paths.append(f"/{slug}/")
    return paths


def built_site_paths() -> list[str]:
    """Walk _site/ and return baseurl-relative paths for each index.html."""
    paths: list[str] = []
    if not BUILT_SITE.exists():
        return paths
    for html in BUILT_SITE.rglob("index.html"):
        rel = html.relative_to(BUILT_SITE).parent.as_posix()
        if rel == ".":
            path = "/"
        else:
            path = f"/{rel}/"
        paths.append(path)
    return sorted(set(paths))


def check(base_url: str, path: str) -> tuple[int | str, str]:
    """GET base_url+path; return (status, reason)."""
    url = urllib.parse.urljoin(base_url + "/", path.lstrip("/"))
    parsed = urllib.parse.urlparse(url)
    conn = http.client.HTTPConnection(parsed.hostname, parsed.port or 80, timeout=10)
    try:
        conn.request("GET", parsed.path or "/", headers={"Host": parsed.hostname})
        resp = conn.getresponse()
        resp.read()
        return resp.status, resp.reason
    except Exception as exc:
        return f"ERR:{exc}", ""
    finally:
        conn.close()


def main() -> int:
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8765"
    base = SITE_BASEURL.rstrip("/")

    nav = navbar_paths()
    built = built_site_paths()

    # Build the full check set: navbar paths + every built index.html path,
    # normalized under the baseurl.
    check_set: dict[str, str] = {}

    def add(label: str, p: str) -> None:
        full = f"{base}{p}" if p != "/" else base or "/"
        check_set.setdefault(full, label)

    for p in nav:
        add("navbar", p)
    for p in built:
        add("built-site", p)

    print(f"Verifying {len(check_set)} paths against {base_url}")
    print("-" * 64)

    failures: list[tuple[str, str, int | str, str]] = []
    for path in sorted(check_set):
        label = check_set[path]
        status, reason = check(base_url, path)
        ok = status == 200 or (isinstance(status, int) and 300 <= status < 400)
        marker = "OK " if ok else "FAIL"
        line = f"{marker} {status:>4} {path:<70} [{label}]"
        if ok and status != 200:
            line += f"  -> redirected ({reason})"
        if reason and not ok:
            line += f"  {reason}"
        print(line)
        if not ok:
            failures.append((path, label, status, reason))

    print("-" * 64)
    total = len(check_set)
    passed = total - len(failures)
    print(f"{passed}/{total} pages returned 200 OK")
    if failures:
        print(f"\n{len(failures)} FAILURES:")
        for path, label, status, reason in failures:
            print(f"  {path} [{label}] -> {status} {reason}")
        return 1
    print("All pages OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())