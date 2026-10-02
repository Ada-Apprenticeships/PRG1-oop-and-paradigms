# Stretch 2: Deciding what can be changed

File: `getters_and_setters.py`

Optional. Not needed for any assignment task.

A plain attribute can be set to anything by anyone. A property lets the class
decide what is allowed.

## Predict

Work out every line of output. The last line of the program does not print
anything, and that is deliberate.

## Run

Execute and compare. The program ends with an error on purpose.

## Investigate

- `_registration` has a leading underscore. Python does not stop you reading it.
  So what is the underscore actually for?
- `days_valid` can be read and written. `registration` can only be read. Which
  decorator makes the difference?
- Two of the three assignments to `days_valid` are rejected. What happens to the
  value in each case, and would you rather it printed, returned something, or
  raised?
- The final line raises an `AttributeError`. Is that better or worse than
  silently ignoring the assignment? Argue it.

## Modify

- Make the rejected assignments raise a `ValueError` rather than printing.
- Add a `zone` attribute that can only be set once.
