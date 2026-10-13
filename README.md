# bench-openai

## Text utilities

`text_utils.py` provides the dependency-free Python helper `slugify(text)`:

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

Run all tests using Python's standard-library test runner:

```sh
python3 -m unittest discover -v
```
