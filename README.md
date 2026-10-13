# bench-openai

## Text utilities

`text_utils.py` provides dependency-free Python text helpers, including
`slugify(text)`:

```python
from text_utils import slugify

slugify("Hello, World!")  # "hello-world"
```

The helper lowercases the input, replaces each run of characters outside
ASCII `a-z` and `0-9` with one hyphen, and trims leading and trailing hyphens.
Empty input and input containing only symbols produce an empty string.

Open review decision: the task does not specify ASCII versus Unicode
alphanumeric handling. The current implementation uses ASCII after lowercasing;
Unicode preservation remains unconfirmed. No transliteration is performed.

`parse_duration(text)` converts compact durations into integer seconds:

```python
from text_utils import parse_duration

parse_duration("90s")       # 90
parse_duration("2m")        # 120
parse_duration("1h30m")     # 5400
parse_duration("1h30m15s")  # 5415
```

The initial grammar accepts positive ASCII integer components without leading
zeros, with each lowercase unit appearing at most once in `h`, `m`, `s` order.
Units may be omitted, and quantities need not be below 60. The entire input must
match; empty strings, unsupported units, negative values, and trailing invalid
text raise `ValueError` with an `Invalid duration` message.

Open review decision: whitespace, uppercase units, decimals, repeated units,
alternate ordering, and zero-valued components or durations remain unspecified.
The initial implementation rejects these forms rather than extending support
without a confirmed requirement. Leading-zero handling also needs confirmation.

Run all tests using Python's standard-library test runner:

```sh
python3 -m unittest discover -v
```
