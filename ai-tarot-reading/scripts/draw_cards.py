#!/usr/bin/env python3
"""Draw tarot cards for a reading.

Deterministic interface, cryptographically random draws. Reads the 78-card
deck from ../assets/cards.json (numbered 1-78).

Usage:
  python3 draw_cards.py --spread three
  python3 draw_cards.py --spread celtic --picks "3, 17 42 5 66 21 8 70 33 12"

--picks accepts the user's raw text in any format; integers are extracted in
order. Invalid input (wrong count, out of range, duplicates) sets
"user_valid": false and missing slots are filled randomly, so the reading can
always proceed.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from random import SystemRandom

SPREAD_COUNTS = {"single": 1, "three": 3, "five": 5, "celtic": 10}

rng = SystemRandom()


def load_deck() -> list[dict]:
    path = Path(__file__).resolve().parent.parent / "assets" / "cards.json"
    with open(path) as fh:
        return json.load(fh)["cards"]


def parse_picks(raw: str, count: int) -> tuple[list[int], bool]:
    nums = [int(m) for m in re.findall(r"\d+", raw or "")]
    valid: list[int] = []
    for n in nums:
        if 1 <= n <= 78 and n not in valid:
            valid.append(n)
    user_valid = len(valid) >= count and len(nums) == count
    picks = valid[:count]
    pool = [n for n in range(1, 79) if n not in picks]
    while len(picks) < count:
        picks.append(pool.pop(rng.randrange(len(pool))))
    return picks, user_valid


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spread", choices=SPREAD_COUNTS, required=True)
    ap.add_argument("--picks", default="")
    args = ap.parse_args()

    count = SPREAD_COUNTS[args.spread]
    deck = {c["pick"]: c for c in load_deck()}

    if args.picks.strip():
        picks, user_valid = parse_picks(args.picks, count)
    else:
        picks = rng.sample(range(1, 79), count)
        user_valid = True

    cards = []
    for i, pick in enumerate(picks, start=1):
        card = deck[pick]
        cards.append(
            {
                "position": i,
                "pick": pick,
                "name": card["name"],
                "arcana": card["arcana"],
                "suit": card.get("suit"),
                "orientation": rng.choice(["upright", "reversed"]),
                "image_url": card["image_url"],
            }
        )

    json.dump(
        {
            "spread": args.spread,
            "count": count,
            "user_valid": user_valid,
            "picked_numbers": picks,
            "cards": cards,
        },
        sys.stdout,
        indent=2,
    )
    print()


if __name__ == "__main__":
    main()
