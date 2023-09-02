# get_distinct_letters

The function `getDistinctLetters` should take two strings and return a string of all the letters that are unique to either of the input strings, in alphabetical order.

## Examples

```py
get_distinct_letters('hello', 'world') # => 'dehrw'

# This is because 'h' and 'e' are in 'hello' but not in 'world', and 'w', 'r' and 'd' are in 'world' but not in 'hello'.
# 'hewrd' sorted => 'dehrw'
```

## Things to think about
- Should lower and upper case letters be considered the same?
- How should non-letter characters be handled?
