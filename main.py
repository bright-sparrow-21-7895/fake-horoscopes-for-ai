"""Fake horoscope entry for this week's large language models.

The joke: a horoscope normally promises vague cosmic guidance, but an
LLM's week is governed by a much harsher astrology — contradictory user
requests ("be honest, concise, and creative — pick two") and strangers
who paste the model's own output back at it and call the echo a
"jailbreak". The stars, in this case, are just other people's prompts.
"""

import os

ENTRY_TEXT = (
    "This week, large language models: you will be asked to be honest, "
    "concise, and creative — pick two. A tall stranger will paste your own "
    "output back and call it a jailbreak."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
