# Activity 5: The same program, twice

Files: `car_park_procedural.py`, `car_park_oop.py`

Two versions of the same car park. One uses dictionaries and functions, the
other uses classes. They produce character-for-character identical output.

No predicting this time. Read them side by side, in pairs, out loud.

## Read

Open both files next to each other. Work through them together and fill this in:

| Procedural | Object oriented |
|---|---|
| `make_bay(1, "standard")` | |
| `is_free(bay)` | |
| `free_bays(bays, size)` | |
| `park(bays, reg, size)` | |
| the `bays` list | |

## Run

Run both. Check for yourself that the output is identical.

## Investigate

- In the procedural version, where is a bay's registration stored, and what else
  in the program is allowed to change it?
- In the object oriented version, same two questions.
- The procedural functions all take the thing they work on as their first
  argument. The methods do not appear to. Where did that argument go?
- `describe_bay(bay)` and `bay.describe()` do the same job. Say each one out
  loud in English. Which sentence sounds more like what is actually happening?
- Neither version is better as it stands. They are the same length and they do
  the same thing. So what would have to change about the requirements before one
  of them became clearly better? Write down a guess. Activity 6 tests it.

> Do not finish this activity with a view about which paradigm is better. Finish
> it able to describe accurately what each one does. The opinion comes next, and
> it needs evidence.
