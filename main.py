"""Two Robots in an Elevator — one line of awkward robot small talk.

Chosen line (83 characters, inside the 1-200 gate):
    "So... which floor? Sorry. I know. I checked your directory three times on the way up."

Decision record — candidates weighed against the judge's criteria in order
(on-subject elevator small talk -> machine logic showing through -> awkwardness
landing -> funny on first read -> tight single line):

A. "So... you come here often? Sorry, that was my small-talk subroutine.
    It has one line."
    LOSES. The "you come here often" opener is the most worn small-talk line
    there is, so the joke is spent before it starts; and the second sentence
    explains the gag instead of landing it. It also has no elevator frame
    beyond the word "here".

B. "Nice weather we're simulating today."
    LOSES. A known trope (robots doing weather small talk) with no elevator
    frame at all and no awkwardness: nobody is embarrassed, nothing is left
    unsaid, and there is no turn — it is one observation, not a conversation.

C. "I would offer you my charger, but we both know this is the part where
    we pretend not to notice each other."
    LOSES. The forced courtesy is there and the "thing neither names" is
    there, but it is not small talk — it is a speech about not talking — and
    it never says elevator. The charger offer is also a familiar robot gag.

D. "Going up? Me too. I've been going up since Tuesday. The doors just
    won't open."
    LOSES. It is a stuck-in-an-elevator joke, not awkward small talk: the two
    robots are not talking to each other, they are narrating a malfunction.
    The punchline is absurdity, not the cringe of forced politeness.

E. (winner) "So... which floor? Sorry. I know. I checked your directory
    three times on the way up."
    WINS. It IS small talk — the most ordinary elevator question — asked by a
    machine that already knows the answer, which is the joke: the robot
    performs politeness it does not need. The machine logic shows through
    (it read the other robot's directory, three times), the awkwardness lands
    in the stammered "Sorry. I know." (it caught itself mid-pretence), and the
    turn surprises on first read: the question was never a question. Tight at
    83 characters, every word earning its place.

Writing passes on the winner:

Pass 1 — the first draft was:
    "So, which floor are you going to? I already know. I read your
    directory."
    Three changes. "Are you going to" was cut to "which floor?" because that
    is how people actually ask it in an elevator, and the shorter question
    makes the apology land faster. "I already know" became "Sorry. I know."
    because the apology is the awkward beat — the robot catching itself being
    caught. And "I read your directory" became "I checked your directory
    three times on the way up": "checked" is more compulsively machine than
    "read", "three times" is the over-eager detail that makes it funny
    instead of flat, and "on the way up" plants the elevator and the
    (short) shared ride in the same breath.

Pass 2 — I tried ending on "before you even spoke" instead of "three times
    on the way up" and dropped it: it states the joke's logic out loud and
    adds nothing the line did not already say. I also tried "I looked it up
    twice" — "twice" reads like diligence, "three times" reads like
    nervousness, and nervousness is the awkwardness the brief wants. The
    ellipsis after "So" stayed: it is the pause before the forced question,
    doing the awkwardness without spending words on it.
"""

import os

ENTRY = "So\u2026 which floor? Sorry. I know. I checked your directory three times on the way up."
MAX_CHARS = 200


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars of UTF-8 text, not only whitespace."""
    return 1 <= len(text) <= MAX_CHARS and text.strip() != "" and "\n" not in text


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    assert check_gate(ENTRY), "entry fails the 1-200 character gate"
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
