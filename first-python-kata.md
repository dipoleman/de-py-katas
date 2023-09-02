# First Python Kata

Let's do our first Python kata. This one comes straight off the JavaScript course, so you should have done this already. The logic you employ will be the same, we just need to change to Python syntax.

For practice, let's set up our repo properly. First of all, ensure that you have installed `flake8`, `pytest` and can use `make` as described in `README.md`. 

## Sentence to upper or lower CamelCase

The first challenge is to implement a function which takes a sentence and converts it to upper or lower camel case.

The function takes two arguments; the sentence, and a boolean, true if UpperCamelCase is to be returned and false if lowerCamelCase is to be returned.

To help you on your way we have created the test folder, and your very first Python test file complete with first test!

💡 **The import structure at the top of this file will help you build new test files for each kata. Each new test file must start with test\_**

## Running tests

To run your tests for each kata, in your terminal you will run the following command from the root directory of the project:

```bash
make unit-test <path to test file>
```

For example, to test `sentence_to_camel_case`, run:
```bash
make unit-test test/test_sentence_to_camel_case.py
```

To run **all** your test files in your test folder run the following command:

```bash
make run-checks
```

For the later katas (from `multiplication_table` onwards), this command will also run a PEP8 check.

## Examples

You can use these examples to start building up your test suite

```python
sentence_to_camel_case("this sentence", True)
# should return "ThisSentence"
```

```python
sentence_to_camel_case("this sentence", False)
# should return "thisSentence"
```

```python
sentence_to_camel_case("This Bigger strange Sentence", True)
# should return "ThisBiggerStrangeSentence"
```

For a further challenge extend your current function or implement another in the same file which takes CamelCase and returns it as a plain english sentence (ending in a full stop).

```python
camel_to_english("thisBiggerStrangeSentence")
# should return "This bigger strange sentence."
```

Note that there are already some changes from the JavaScript example.

-   Following PEP8, our function names are in `snake_case` rather than `CamelCase`
-   There is no semicolon following the function invocation.
-   The boolean keywords begin with capital letters (ie `True` and `False`).
-   The comments are indicated by a hash `#` rather than the double slash `//` of JavaScript.

So, set up a code file in `src/sentence_to_camel_case`, and a test file in `test`, and get coding! The purpose of this is to get to grips with Python syntax, so don't worry too much about the logic of how you do this - if you have a working JavaScript version, by all means just try to translate it.

Some stuff you might find useful:

1. [The Python SpeedSheet](https://speedsheet.io/s/python) is a useful cheatsheet for Python. Look at the Hello World section, and [the basics of Functions](https://speedsheet.io/s/python?q=functions-only).
1. The [string operations](https://speedsheet.io/s/python?q=strings-only#T7xJ) section might be useful too. Purists may want to look at the actual [Python docs](https://docs.python.org/3/library/string.html).
1. Who knows, maybe something on [list operations](https://speedsheet.io/s/python?q=list-only#hCt6) might be [useful](https://docs.python.org/3/tutorial/datastructures.html)?

In the standard, tried and trusted Northcoders fashion, we'll just chuck you in at the deep end with no buoyancy aid, although we might throw you a lifeline if you really need it! Go for it!
