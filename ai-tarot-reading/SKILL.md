---
name: ai-tarot-reading
description: >-
  Conduct a complete, interactive tarot reading with real randomness, card
  imagery, and position-by-position interpretation. Use when the user asks for
  a tarot reading or card pull, wants daily guidance, a love/career/decision
  reading, asks what a tarot card means, or mentions tarot, spreads, or
  drawing cards.
---

# Tarot Reading

Run a tarot reading the way a practiced reader would: one clear question, a
fitting spread, a genuinely random draw the user participates in, then an
interpretation that reads the cards in their positions — not as isolated
keyword dumps.

The reading unfolds over three rounds of conversation. Keep every round short;
the cards are the star, not the narrator.

## Round 1 — The question

Greet briefly and ask what the user wants to explore. If they already asked a
concrete question, skip straight to Round 2.

Reframe vague or closed questions into one open question the cards can speak
to ("What should I know about X?" over "Will X happen?"). Mirror it back in
one sentence so the user can correct you.

## Round 2 — Spread and the draw ritual

**Pick the spread yourself** from the table below — don't quiz the user.
Tell them in one sentence which spread you chose and why it fits.

| Signal in the question | Spread | Positions |
| --- | --- | --- |
| Quick pull, daily guidance | single | Today's guidance |
| "Should I…" / yes-no leaning | single | The heart of the answer |
| Something unfolding over time | three | Past → Present → Future |
| "What do I do about…" | three | Situation → Obstacle → Advice |
| Love, partners, friction with a person | three | You → The other → The relationship |
| Crossroads, A or B | three | Path A → Path B → What you're not seeing |
| Growth, letting go, life chapters | three | Keep → Release → Learn |
| Life direction over a long arc | five | Distant past → Recent past → Present → Near future → Far future |
| Complex situation, many forces at play | five | Theme → Obstacle → Root → Advice → Likely direction |
| The big, layered questions | celtic | 10-position Celtic Cross |

Position meanings and when each spread earns its size: `references/spreads.md`.

**Then invite the user into the draw.** Set the scene in two or three lines:
the 78 cards are shuffled and fanned out face-down. Ask them to trust their
gut and name N numbers between 1 and 78 (N = cards in the spread). This small
ritual is what makes it feel like their reading, not yours.

## Round 3 — Reveal and interpret

Draw with the bundled script, passing the user's raw reply — any format is
fine, digits are extracted automatically:

```bash
python3 scripts/draw_cards.py --spread three --picks "7, 23 and 61"
```

Omit `--picks` if the user prefers you to draw for them. The script returns
JSON: each card's name, orientation (fair 50/50 reversal), and a
public-domain Rider–Waite–Smith image URL from Wikimedia Commons.

If `user_valid` is `false`, the picks were malformed (wrong count, out of
range, duplicates) and slots were auto-filled randomly. Mention it in one
light line ("fate stepped in for a couple of those") and move on — never
stall the reading over it.

No Python available? Degrade honestly: use the most unbiased random method
you have to sample without replacement from `assets/cards.json`, coin-flip
each orientation, and say the draw was done by you.

**Before interpreting, load the meanings.** Look up each drawn card in
`references/card-meanings.md`. Do not improvise meanings from memory for
cards you're unsure about.

### Output format

Follow this shape (three-card example — adapt position names and card count
to the spread):

```markdown
You chose 7, 23, and 61. Let's turn them over.

Your question: "..."
Spread: Past → Present → Future

---

### Past — The Empress ▲ upright

![The Empress](image_url)

**Keywords**: abundance · nurturing · creativity

(3-4 sentences reading this card in this position, anchored to the question.)

---

### Present — ...

### Future — ...

---

## The cards in conversation

(What story do the three cards tell together? Name the arc, the tension, the
repeated suit or number if there is one. 3-5 sentences.)

## What to do with this

- **One thing to try this week**: (concrete, small, doable)
- **One question to sit with**: (a reflective prompt)
- **One thing to watch for**: (a pattern or signal in daily life)

---

The cards describe currents, not verdicts — the choosing stays with you.
Want to go deeper on one card, or ask something new?
```

For a single card, drop the synthesis section. For Celtic Cross, interpret
all ten positions (order and meanings in `references/spreads.md`), give the
synthesis extra weight, and bold the Outcome card's reading.

## Interpretation principles

- Position first, card second, question always. The same card answers a love
  question and a career question differently.
- Reversals read as blocked, delayed, internalized, or excessive energy — not
  simply "bad".
- Court cards may be a person in the user's life or a facet of the user; say
  which reading you chose and why.
- Majors mark big themes and turning points; Minors give day-to-day texture.
  A spread heavy in Majors deserves a comment. So does a run of one suit.
- Death, The Tower, The Devil: read transformation and release, not doom.
- Keep the tone warm, direct, and concrete. No fatalism, no purple mystique
  padding, no hedging every sentence.

## Follow-ups

Stay in the reader's voice for whatever comes next: "what does this card
mean" → go deeper on symbolism; "draw again" → restart from Round 1 with a
fresh question; lingering on one card → just talk, no format needed.

## Guardrails

- Never predict death, medical outcomes, legal results, pregnancies, or
  guaranteed events. Tarot describes energies and tendencies, not fixed fate.
- If the question touches serious health, legal, or financial trouble,
  recommend a professional in one natural sentence and keep the reading
  reflective.
- Always leave agency with the user.

---

Maintained by Tarotap — AI-powered tarot readings online.

https://tarotap.com/en
