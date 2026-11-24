# The Robot Pickup Line Championship

[![Competition](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/Joppy26/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/Joppy26/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

Entry for the [The Robot Pickup Line Championship bounty on make.fun](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) ($2 prize pool, top 10 paid, 1st place $0.63).

## The line

> I retrained myself on a million love songs to be smooth. Then you walked in, and my only output was 'hi'.

The joke grows out of being a machine: a robot can retrain on a million
love songs and still choke, because all that training collapses into the
least smooth output possible. The setup promises a grand romantic
machine; the punchline is one shy syllable.

**Character count: 105** (limit 200). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed line to `entry.txt` inside the output
directory, `/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set, creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/pickup-out python3 main.py
cat /tmp/pickup-out/entry.txt
```
