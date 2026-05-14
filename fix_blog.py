import json

files = ["blog/fixtures/blog.json", "blog/fixtures/sector_articles.json"]

replacements = [
    ("\u2014", "-"),
    ("\u2013", "-"),
    ("\u2019", "'"),
    ("\u2018", "'"),
    ("\u201c", '"'),
    ("\u201d", '"'),
    ("\u00e2\u0080\u0094", "-"),
    ("\u00e2\u0080\u0093", "-"),
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed: {filepath}")

print("Done")
