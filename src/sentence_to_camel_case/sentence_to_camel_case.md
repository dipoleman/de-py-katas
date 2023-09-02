# sentence_to_camel_case

The challenge is to implement a function which takes a sentence and converts it to upper or lower camel case

The function takes two arguments; the sentence, and a boolean, true if UpperCamelCase is to be returned and false if lowerCamelCase is to be returned

## Examples

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
## Other cases to think about

```python
sentence_to_camel_case("WHY ARE YOU YELLING", True)
sentence_to_camel_case("tHiS iS a BiT oDd", True)
sentence_to_camel_case("these 1 include 2 numbers 3", True)
# what do you think should happen here?
```

## Further Challenge
For a further challenge extend your current function or implement another in the same file which takes CamelCase and returns it as a plain english sentence (ending in a full stop).

```python
camel_to_english("thisBiggerStrangeSentence")
# should return "This bigger strange sentence."
```
