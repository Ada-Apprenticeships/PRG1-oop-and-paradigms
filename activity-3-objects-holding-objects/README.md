# Activity 3: Objects holding objects

File: `car_park.py`

A working program, and the shape that matters most today. A `CarPark` does not
hold registrations. It holds `Bay` objects, and each `Bay` looks after its own.

## Predict

From the code alone, work out:

- Which bays are free before anything is parked?
- Which bay does each of the three cars get?
- Which bays are free afterwards?
- What does `find` return for a car that is not there?

## Run

Execute and compare.

## Investigate

- `CarPark.park` does not set a registration itself. It finds a suitable bay and
  asks the bay to do it. Why is that better than reaching in and setting
  `bay.registration` directly?
- `add_bay` creates a `Bay` inside `CarPark`. Nothing outside ever sees the
  `Bay` class being used. Is that a good thing or a limitation? Argue both.
- `report` builds a list of lines and joins them. Each line comes from
  `bay.describe()`. If you wanted to change how a bay is displayed, how many
  places would you have to change?
- `find` compares `bay.registration == registration`. That works because a
  registration is a string. Hold that thought until activity 4.

## Modify

- Add a method that reports how many bays of each size are free.
- Add a `leave(registration)` method on `CarPark` that frees the right bay.
- Add a fifth bay of a new size and predict every figure that changes.

> This is the same shape as the program in this afternoon's assignment task: one
> object that holds many objects, and asks them things rather than reaching
> inside them.
