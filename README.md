# Demo Assisted Tests

A demonstration of using ChatGPT to revise code functionality and implement viable tests.

Files at a glance:
- `original.py` -- the original script that was used for a Redis use-case and its potential memory footprint assessment.
- `revised.py` -- revised version of `original.py` using ChatGPT suggestions.
- `unit.test.py` -- ChatGPT suggested unit test of one of the functions it extracted in `revised.py`
- `mock.test.py` -- ChatGPT suggested integration test by stubbing the Redis usage with Python's magic mock capability

The ChatGPT interaction (sped up 4x, original video was ~12 minutes in length):

https://user-images.githubusercontent.com/2837532/225130937-fbb53ca8-62d2-4c95-8e1e-147c5c0da0fd.mov

Some follow-up interactions for it to revise the mock test:

![mock](https://user-images.githubusercontent.com/2837532/225131146-c0227f45-fcad-4833-9777-5b6526834fe9.png)
