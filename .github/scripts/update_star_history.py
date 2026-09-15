"""Append a daily repository star-count snapshot and render its SVG chart."""

import argparse
import csv
import json
import os
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "Robinson-AI-Lab/FridayOS1.0")
SNAPSHOTS = Path("docs/data/star-history.csv")
OUTPUT = Path("docs/images/star-history.svg")
WIDTH, HEIGHT = 900, 420
LEFT, TOP, RIGHT, BOTTOM = 70, 35, 25, 55


def fetch_current_count():
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
        "User-Agent": "FridayOS1.0-star-history",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}", headers=headers
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            count = json.load(response)["stargazers_count"]
    except (urllib.error.HTTPError, urllib.error.URLError, KeyError) as error:
        raise SystemExit("Unable to read the repository's current star count") from error

    if not isinstance(count, int) or count < 0:
        raise SystemExit(f"Invalid repository star count: {count!r}")
    return count


def read_snapshots():
    if not SNAPSHOTS.exists():
        return []

    snapshots = []
    with SNAPSHOTS.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ["date", "stars"]:
            raise SystemExit("Snapshot file must have date,stars columns")
        try:
            for row in reader:
                snapshots.append((date.fromisoformat(row["date"]), int(row["stars"])))
        except (TypeError, ValueError) as error:
            raise SystemExit("Snapshot file contains invalid data") from error

    if not snapshots:
        raise SystemExit("Snapshot file must contain at least one observation")
    if snapshots != sorted(snapshots) or len({day for day, _ in snapshots}) != len(
        snapshots
    ):
        raise SystemExit("Snapshots must be unique and sorted by date")
    if any(count < 0 for _, count in snapshots):
        raise SystemExit("Snapshot counts cannot be negative")
    return snapshots


def update_snapshot(snapshots, snapshot_date, count):
    if snapshots and snapshot_date < snapshots[-1][0]:
        raise SystemExit(
            "Refusing to rewrite historical snapshots with an earlier observation"
        )
    if snapshots and snapshot_date == snapshots[-1][0]:
        snapshots[-1] = (snapshot_date, count)
    else:
        snapshots.append((snapshot_date, count))
    return snapshots


def write_snapshots(snapshots):
    SNAPSHOTS.parent.mkdir(parents=True, exist_ok=True)
    with SNAPSHOTS.open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(["date", "stars"])
        writer.writerows((day.isoformat(), count) for day, count in snapshots)


def render(snapshots):
    start, end = snapshots[0][0], snapshots[-1][0]
    span = max((end - start).days, 1)
    plot_w = WIDTH - LEFT - RIGHT
    plot_h = HEIGHT - TOP - BOTTOM
    maximum = max(count for _, count in snapshots)
    scale_max = max(maximum, 1)

    points = []
    for day, count in snapshots:
        x = LEFT + ((day - start).days / span) * plot_w
        y = TOP + plot_h - (count / scale_max) * plot_h
        points.append((x, y))

    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    area = f"{LEFT},{TOP + plot_h} {line} {LEFT + plot_w},{TOP + plot_h}"
    markers = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" class="point"/>'
        for x, y in points
    )

    grid = []
    for step in range(5):
        y = TOP + plot_h - step * plot_h / 4
        value = round(scale_max * step / 4)
        grid.append(
            f'<line x1="{LEFT}" y1="{y:.1f}" x2="{LEFT + plot_w}" '
            f'y2="{y:.1f}" class="grid"/>'
        )
        grid.append(
            f'<text x="{LEFT - 12}" y="{y + 5:.1f}" text-anchor="end" '
            f'class="label">{value}</text>'
        )

    current = snapshots[-1][1]
    start_label = start.isoformat()
    end_label = end.isoformat()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">FridayOS1.0 Star History</title>
<desc id="desc">{len(snapshots)} observed star-count snapshots from {start_label} to {end_label}; current count {current}</desc>
<style>
  .bg {{ fill: #ffffff; }} .grid {{ stroke: #e5e7eb; stroke-width: 1; }}
  .label {{ fill: #6b7280; font: 13px system-ui, sans-serif; }}
  .title {{ fill: #111827; font: 600 20px system-ui, sans-serif; }}
  .area {{ fill: #6366f1; opacity: .12; }} .line {{ fill: none; stroke: #4f46e5; stroke-width: 3; }} .point {{ fill: #4f46e5; }}
  @media (prefers-color-scheme: dark) {{ .bg {{ fill: #0d1117; }} .grid {{ stroke: #30363d; }} .label {{ fill: #8b949e; }} .title {{ fill: #f0f6fc; }} .area {{ fill: #818cf8; }} .line {{ stroke: #818cf8; }} .point {{ fill: #818cf8; }} }}
</style>
<rect class="bg" width="100%" height="100%" rx="10"/>
<text x="{LEFT}" y="25" class="title">Star History · {current} stars</text>
{''.join(grid)}
<polygon points="{area}" class="area"/><polyline points="{line}" class="line"/>{markers}
<text x="{LEFT}" y="{HEIGHT - 18}" class="label">{start_label}</text>
<text x="{LEFT + plot_w}" y="{HEIGHT - 18}" text-anchor="end" class="label">{end_label}</text>
</svg>
'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="\n") as output:
        output.write(svg)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, help="use a supplied count for testing")
    parser.add_argument("--date", type=date.fromisoformat, default=date.today())
    return parser.parse_args()


def main():
    args = parse_args()
    count = args.count if args.count is not None else fetch_current_count()
    if count < 0:
        raise SystemExit("Star count cannot be negative")
    snapshots = update_snapshot(read_snapshots(), args.date, count)
    write_snapshots(snapshots)
    render(snapshots)


if __name__ == "__main__":
    main()
