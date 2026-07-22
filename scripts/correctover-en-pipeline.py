#!/usr/bin/env python3
"""
Correctover English Content Pipeline v1.1
Uses curl (Dev.to API connectivity is reliable via curl from this network).
Schedule: weekly (Saturday 9AM UTC) — publish one article per run.
"""
import json, os, subprocess, sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

DEVT0_API_KEY = "eKxpfcnQHYxicqSdBa1YdDnT"
TRACKER_PATH = r"C:\d\workspace\correctover-en-tracker.json"
MAX_TAGS = 4

CONTACT_BLOCK = """

---

**Correctover** — AI Runtime Security
- Real-time RCE, SSRF & Credential Protection in **14.5µs**
- **24 CCS** detection rules · **80K** production traces · **4,709** validated findings
- [correctover.com/en](https://correctover.com/en) · [GitHub](https://github.com/correctover/mcp-server)

*This article is for informational purposes. Vulnerability findings are from responsible disclosure programs. Benchmark data from Correctover internal testing.*
"""

ARTICLES = [
    {"id": 2, "title": "From Bounty to Defense: How 7 RCE Disclosures Shaped Production Detection Rules",
     "tags": ["security", "ai", "bugbounty", "infosec"], "published": False, "file": "article-2.html"},
    {"id": 3, "title": "CCS Compliance for AI Systems: A 24-Rule Framework for Production Security",
     "tags": ["security", "compliance", "cloud", "infosec"], "published": False, "file": "article-3.html"},
    {"id": 4, "title": "The AI Runtime Attack Surface: 7 Threats Every CISO Should Know",
     "tags": ["security", "ciso", "cloud", "infosec"], "published": False, "file": "article-4.html"},
]

BLOG_DIR = r"C:\d\workspace\correctover\web\blog"

def load_tracker():
    try:
        with open(TRACKER_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"articles": ARTICLES, "next_index": 0, "total_published": 0,
                "created": datetime.now().isoformat()}

def save_tracker(tracker):
    with open(TRACKER_PATH, "w") as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)

def extract_title(html_path):
    import re
    with open(html_path, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"<h1>(.*?)</h1>", content, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r"<title>(.*?)</title>", content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return "Correctover Security Article"

def publish_via_curl(title, body_md, tags, canonical_url):
    import tempfile
    payload = json.dumps({
        "article": {
            "title": title,
            "published": True,
            "body_markdown": body_md,
            "tags": tags[:MAX_TAGS],
            "series": "AI Runtime Security",
            "canonical_url": canonical_url,
        }
    })
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
    tmp.write(payload)
    tmp.close()
    try:
        result = subprocess.run([
            "curl", "-s", "-X", "POST", "https://dev.to/api/articles",
            "-H", f"api-key: {DEVT0_API_KEY}",
            "-H", "Content-Type: application/json",
            "-d", f"@{tmp.name}",
            "--connect-timeout", "10", "--max-time", "30"
        ], capture_output=True, text=True, timeout=45)
        os.unlink(tmp.name)
        return json.loads(result.stdout)
    except Exception as e:
        os.unlink(tmp.name)
        return {"error": str(e)}

def main():
    tracker = load_tracker()
    idx = tracker["next_index"]
    article_list = tracker["articles"]

    if idx >= len(article_list):
        print("[EN Pipeline] All articles published. Done.")
        return

    article = article_list[idx]
    if article["published"]:
        tracker["next_index"] = idx + 1
        save_tracker(tracker)
        print(f"[EN Pipeline] Article {article['id']} already published, skipping.")
        return

    print(f"[EN Pipeline] Publishing #{article['id']}: {article['title']}")

    body_md = f"# {article['title']}\n\nFull article: https://correctover.com/en/blog/{article['file']}\n\n---\n\n" + CONTACT_BLOCK
    canonical = f"https://correctover.com/en/blog/{article['file']}"

    resp = publish_via_curl(article["title"], body_md, article["tags"], canonical)

    if resp.get("url"):
        article["published"] = True
        article["url"] = resp["url"]
        tracker["total_published"] += 1
        tracker["next_index"] = idx + 1
        tracker["last_published"] = datetime.now().isoformat()
        save_tracker(tracker)
        print(f"[EN Pipeline] Published: {resp['url']}")
    else:
        print(f"[EN Pipeline] Failed: {resp.get('error', resp)}")

if __name__ == "__main__":
    main()
