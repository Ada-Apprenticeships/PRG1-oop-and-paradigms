# Activity 2: Two objects, one class

File: `two_bays.py`

The same class used twice, and then a third name pointing at one of them.

## Predict

Write down every line of output. The last two are the ones to think hardest
about.

## Run

Execute and compare.

## Investigate

- `first` and `second` came from the same class. After `first.park(...)`, only
  one of them has a registration. Where is each bay's registration actually
  stored?
- `first.park("AB12 CDE")` never mentions `self`, and yet `self` inside the
  method refers to `first`. Work out how. Then predict what `self` would be
  during `second.describe()`.
- `third = second` did not make a third bay. You met this on Day 5 with
  playlists and on Day 8 with grids. What does assignment actually copy?
- How many `Bay` objects exist by the end of the program? The answer is not
  three.

## Modify

- Add a fourth bay and park a car in it without touching the other three.
- Write a loop that describes all the bays, without naming them individually.
- Make `third` a genuinely separate bay rather than another name for `second`.

> Two objects made from one class have their own copies of every attribute.
> Two names pointing at one object do not.
