# Activity 6: The change experiment

Files: `car_park_procedural.py`, `car_park_oop.py` (your own copies)

Paired, and the most useful hour of the day. You are going to make the **same
two changes** to **both** versions, and record what actually happened.

This is not a tidy exercise with a right answer. It is evidence gathering, and
the evidence is what this afternoon's assignment task asks you to reason from.

## How to run it

- Work in pairs, one driving, swapping at each change.
- Do each change to one version, then the same change to the other version.
- Time yourselves roughly. Minutes, not seconds.
- Fill the table in as you go, not afterwards. You will not remember accurately.

## Change A: remember every car that has used a bay

Each bay should keep a record of every registration that has parked in it, in
order, and you should be able to ask a bay for that history.

Do it in both versions.

| | Procedural | Object oriented |
|---|---|---|
| How many places did you have to change? | | |
| Roughly how long? | | |
| What did you have to remember to do? | | |

Then answer this, which is the real question: **in each version, could some
other part of the program park a car without the history being updated?** Try
it. Write down what you find.

## Change B: write the bay data out to a file

The operations team want a plain text file with one line per bay, so a different
system can read it in. Fields separated by commas: number, size, registration or
the word `free`.

Do it in both versions.

| | Procedural | Object oriented |
|---|---|---|
| How many places did you have to change? | | |
| Roughly how long? | | |
| What got in your way? | | |

## What to write down before you leave

Three sentences, in your own words, in your repository:

1. One thing the object oriented version made genuinely easier, with the
   evidence from change A.
2. One thing the procedural version made genuinely easier, with the evidence
   from change B.
3. Which version you would rather extend if the car park had to handle three
   sites, two kinds of permit and a waiting list, and why.

Keep these. They are most of the answer to the task released this afternoon,
and they will be far better than anything you can write from memory next week.

> There is no correct answer to the third question. A strong answer argues
> either way with specifics. A weak answer repeats something a lecturer said.
