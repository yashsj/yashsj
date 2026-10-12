import json
import math
import os
import random
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

USERNAME = os.environ.get("GITHUB_USERNAME", "yashsj")
TOKEN = os.environ["GITHUB_TOKEN"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            weekday
            contributionCount
            contributionLevel
          }
        }
      }
    }
  }
}
"""

LEVELS = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}

THEMES = {
    "dark": {
        "background": "#0d1117",
        "empty": "#161b22",
        "text": "#8b949e",
        "colors": ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"],
    },
    "light": {
        "background": "#ffffff",
        "empty": "#ebedf0",
        "text": "#57606a",
        "colors": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"],
    },
}

CELL = 11
GAP = 4
STEP = CELL + GAP
LEFT = 28
TOP = 125
CYCLE = 10.0


def fetch_calendar():
    payload = json.dumps({
        "query": QUERY,
        "variables": {"login": USERNAME},
    }).encode()

    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "falling-contribution-grid",
        },
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)

    if result.get("errors"):
        raise RuntimeError(json.dumps(result["errors"]))

    user = result.get("data", {}).get("user")
    if not user:
        raise RuntimeError(f"GitHub user not found: {USERNAME}")

    return user["contributionsCollection"]["contributionCalendar"]


def render_svg(calendar, theme_name):
    theme = THEMES[theme_name]
    weeks = calendar["weeks"]
    width = LEFT * 2 + len(weeks) * STEP - GAP
    height = TOP + 7 * STEP + 35

    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img">',
        '<title>Contribution squares falling into place</title>',
        '<desc>Colored squares fall and settle into a contribution calendar.</desc>',
        f'<rect width="{width}" height="{height}" rx="12" '
        f'fill="{theme["background"]}"/>',
        f'<text x="{LEFT}" y="28" fill="{theme["text"]}" '
        f'font-family="monospace" font-size="12">'
        f'{escape(USERNAME)} · '
        f'{calendar["totalContributions"]:,} contributions'
        '</text>',
    ]

    active = []

    # Draw the empty calendar first, underneath every falling square.
    for column, week in enumerate(weeks):
        for day in week["contributionDays"]:
            x = LEFT + column * STEP
            y = TOP + day["weekday"] * STEP

            pieces.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" '
                f'height="{CELL}" rx="2" fill="{theme["empty"]}"/>'
            )

            level = LEVELS[day["contributionLevel"]]
            if level:
                active.append((x, y, day, level))

    for x, y, day, level in active:
        # Stable randomness: both themes have identical movement.
        rng = random.Random(f'{USERNAME}:{day["date"]}')

        start_y = rng.uniform(43, 92)
        offset_x = rng.uniform(-18, 18)
        distance = y - start_y

        # Uniform acceleration from rest: distance = 0.5 * g * t^2.
        gravity = 700.0
        fall_time = math.sqrt(2 * distance / gravity)
        delay = rng.uniform(0.2, 2.0)

        times = [0.0, delay / CYCLE]
        positions = [
            (offset_x, -distance),
            (offset_x, -distance),
        ]

        # Sample the trajectory instead of relying on browser physics.
        for sample in range(1, 13):
            progress = sample / 12
            elapsed = delay + fall_time * progress
            times.append(elapsed / CYCLE)
            positions.append((
                offset_x * (1 - progress),
                -distance * (1 - progress * progress),
            ))

        landed = delay + fall_time

        # Small stylized bounce, settle, then hold.
        times.extend([
            (landed + 0.10) / CYCLE,
            (landed + 0.23) / CYCLE,
            (landed + 0.31) / CYCLE,
            (landed + 0.40) / CYCLE,
            1.0,
        ])
        positions.extend([
            (0, -4),
            (0, 0),
            (0, -1),
            (0, 0),
            (0, 0),
        ])

        key_times = ";".join(f"{t:.6f}" for t in times)
        values = ";".join(
            f"{dx:.3f} {dy:.3f}" for dx, dy in positions
        )

        tooltip = escape(
            f'{day["date"]}: {day["contributionCount"]} contributions'
        )

        pieces.append(
            f'<g transform="translate({x} {y})">'
            f'<rect width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{theme["colors"][level]}" '
            f'transform="translate({offset_x:.3f} {-distance:.3f})">'
            f'<title>{tooltip}</title>'
            f'<animateTransform attributeName="transform" '
            f'type="translate" calcMode="linear" '
            f'values="{values}" keyTimes="{key_times}" '
            f'dur="{CYCLE}s" repeatCount="indefinite"/>'
            '</rect></g>'
        )

    pieces.append('</svg>')
    return "\n".join(pieces)


def main():
    calendar = fetch_calendar()
    output = Path("dist")
    output.mkdir(exist_ok=True)

    for theme in THEMES:
        destination = output / f"contribution-grid-{theme}.svg"
        destination.write_text(
            render_svg(calendar, theme),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
