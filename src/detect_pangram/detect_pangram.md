# detect_pangram

A pangram is a sentence that contains every single letter of the alphabet at least once.

For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

The function `detect_pangram` should accept a string and return a boolean value representing whether or not it is a pangram.

## Examples

```py
detect_pangram("The quick brown fox jumps over the lazy dog.") # True

detect_pangram("This is not a pangram.") # False
```
