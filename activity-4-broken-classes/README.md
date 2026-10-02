# Activity 4: Broken classes

File: `broken_classes.py`

Three classes, three faults. Nothing crashes, and every answer looks like an
answer.

## Predict

Work out what each part **should** produce:

1. Two separate waiting lists, one with two cars on it and one with one.
2. A barrier that starts closed and is open after `open_barrier()`.
3. A permit check that says yes for AB12 CDE in zone A and no for QQ11 QQQ.

## Run

Execute it. All three are wrong.

## Investigate

- Both waiting lists report three. There are only three cars in total. Look at
  where `waiting` is defined compared with where `name` is defined. One of them
  is inside `__init__` and one is not. What difference does that make?
- The barrier never opens and nothing errors. Read `open_barrier` one word at a
  time, then compare it with `__init__`. Something is missing.
- The permit check says no for a car that plainly has a permit. `has_permit`
  builds a brand new `Permit` and asks whether it is `in` the list. What does
  `in` compare, and are two permits with the same registration the same object?

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. North should report 2, South 1, the barrier should open, and the
permit check should say `True` then `False`.

For the third one there is more than one defensible fix. Write down in your
fault log which you chose and why.

> The first fault is the most common mistake in beginner class code and the
> hardest to see, because the line that causes it looks perfectly ordinary. An
> attribute belongs in `__init__` unless you deliberately want every object to
> share one.
