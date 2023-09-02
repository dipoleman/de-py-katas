# crack_code

For this task we are going to need to decrypt an encrypted key to find out whether it is a valid key.

A key is valid if the 4 most common letters in the part before the brackets are in alphabetical order within in the brackets.

**Examples of valid codes:**

```py
"ddd-aaa-z-y-x-123(adxy)"
"a-b-c-d-e-f-g-h-i-577(abcd)"
"fff-gg-xx-ss-y(fgsx)"
```

**An example of an invalid codes might be:**

```py
"a-b-c-d-e-f-g-h-i-577(acdb)" # The code in brackets is not in the alphabetical order
"fff-gg-xx-ss-y(fgsy)" # Although fgsy is alphabetical, x is more common than y
```

The function should return true if code is valid or false if it is not.

---

## Examples

```py
crack_code("ddd-aaa-z-y-x-123(adxy)");
# true
```

```py
crack_code("a-b-c-d-e-f-g-h-i-577(abcd)");
# true
```

```py
crack_code("fff-gg-xx-ss-y(fgsy)");
# false
```
