# A simple coding challenge

Given an array split it up in the middle and add each elements to create a new
array. Continue the process to reduce to a single number. That is, sum up the
elements of the array by splitting up it in the middle each time and adding the
splitted array together.

Following is an example program flow:

    [33, 6, 9, 1, 23, 88, 2]
    => [33, 6, 9] + [1, 23, 88, 2]
    => [1, 56, 94, 11]
    => [1, 56] + [94. 11]
    => [95, 67]
    => [162]

This is implemented in python and javascript with unit tests.

# Python

Python implementation is in `reduce.py` and the unit test is in
`test_reduce.py`. To run the tests either python2 or python3 should be
installed and can be run by `python test_reduce.py` or
`python3 test_reduce.py`.

# JavaScript

Javascript implementation is in `reduce.js` file, it is implemented in modern
or es2015 syntax. To run it nodejs 8+ or modern browsers are required. The unit
tests are written in `jest` test framework. To run the tests the environment
need to be initialised. After that one can run the tests.

    $ npm install
    $ npm test
