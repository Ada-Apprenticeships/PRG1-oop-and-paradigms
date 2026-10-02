# Stretch 1: One class built on another

File: `inheritance.py`

Optional. Not needed for any assignment task, and worth reaching only once the
core activities are done.

An `ElectricBay` is a `Bay` that also knows about a charger.

## Predict

Six lines of output. The last two are the ones to think about.

## Run

Execute and compare.

## Investigate

- `ElectricBay` never defines `is_free`, and yet `electric.is_free()` works.
  Where did that method come from?
- `super().park(registration)` calls the `Bay` version, then `ElectricBay` does
  something extra. Why call the original at all rather than writing it out
  again?
- `isinstance(electric, Bay)` is `True`. An electric bay is a bay. Is a bay an
  electric bay? Check.
- `describe` exists on both classes. Which one runs, and how does Python decide?

## Modify

- Add a `DisabledBay` that requires a permit number before parking.
- Make `ElectricBay` refuse to park a car if the charger is broken.

> Inheritance is powerful and frequently misused. The usual test is whether the
> new thing genuinely *is a* kind of the old thing in every situation the
> program cares about. If you find yourself overriding most of the parent, it
> probably is not.
