#!/usr/bin/env python3
"""Change the site's main address everywhere in one go.

Usage:  python3 tools/set-domain.py movilang.pl
        python3 tools/set-domain.py movilang.pages.dev

- replaces the current address in index.html, sitemap.xml, robots.txt, 404.html, README.md
- sets MOVILANG_SITE.URL in config.js
- adds the old host to REDIRECT_FROM, so visitors of the old address are sent to the new one
"""
import os, re, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) != 2: sys.exit(__doc__)
new = sys.argv[1].strip().rstrip("/")
if not new.startswith("http"): new = "https://" + new
new_host = re.sub(r"^https?://", "", new)
cfg_path = os.path.join(ROOT, "config.js"); cfg = open(cfg_path, encoding="utf-8").read()
old = re.search(r'URL:\s*"([^"]+)"', cfg).group(1).rstrip("/")
old_host = re.sub(r"^https?://", "", old)
if old == new: sys.exit("Already " + new)
for f in ["index.html", "sitemap.xml", "robots.txt", "404.html", "README.md"]:
    p = os.path.join(ROOT, f)
    if not os.path.exists(p): continue
    s = open(p, encoding="utf-8").read(); n = s.count(old)
    open(p, "w", encoding="utf-8").write(s.replace(old, new)); print(f"{f}: {n} replaced")
m = re.search(r"REDIRECT_FROM:\s*(\[[^\]]*\])", cfg)
hosts = json.loads(m.group(1)); hosts = [h for h in hosts if h != new_host]
if old_host not in hosts: hosts.append(old_host)
cfg = cfg.replace(m.group(0), "REDIRECT_FROM: " + json.dumps(hosts))
cfg = re.sub(r'URL:\s*"[^"]+"', f'URL: "{new}"', cfg, count=1)
open(cfg_path, "w", encoding="utf-8").write(cfg)
print("config.js: URL =", new, "| redirect from:", hosts)
print("Next: bump ?v= in index.html, commit, push. Then Supabase -> Auth -> URL Configuration.")
