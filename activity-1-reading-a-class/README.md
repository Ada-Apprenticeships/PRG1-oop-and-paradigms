# Activity 1: Reading a class

File: `bay.py`

One class, describing a single parking bay. Read it before you run it.

## Predict

Nine lines of output. Write them all down. Pay particular attention to the two
`park` calls: one of them does something and one of them does not.

## Run

Execute and compare.

## Investigate

- `Bay` is the description. `bay = Bay(1, "standard")` makes one actual bay from
  it. Which lines of the class run at the moment that happens?
- `self` appears in every method. Replace `self.registration` with `registration`
  in `is_free` and run it. Read the error. What is `self` actually standing in
  for?
- `park` returns `True` or `False` rather than printing anything. Why is that
  more useful than printing "parked" inside the method?
- `describe` reads `self.registration` but never changes it. `leave` changes it.
  Which methods ask the bay something, and which tell it to do something?

## Modify

- Add a `size_matches(wanted)` method that says whether this bay is the right
  size.
- Make `leave` return `None` and print a message if the bay was already empty.
- Add an attribute recording how many cars have used this bay, and update it in
  the right place.

> A class is a description of a kind of thing: what it knows about itself, and
> what it can be asked to do. Everything else today is built on that sentence.
