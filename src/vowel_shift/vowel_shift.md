# vowel_shift

Given a string of any length and a number `n`, shift every vowel in the string `n` vowel positions to the right. The final vowel in the string wraps round and goes back to the beginning of the string.

For example, in the string 'hello child', if each vowel was shifted 1 vowel position to the right, the `e` would move to the `o`'s position, the `o` would move to the `i`'s position, and the `i` would wrap back round and fill the `e`'s position, giving:

```py
'hille chold'
```

## Examples

```py
vowel_shift('foo', 1);
  # 'foo'
```

```py
vowel_shift('hello', 1);
  # 'holle'
```

```py
vowel_shift('hello child', 1);
  # 'hille chold'
```

```py
vowel_shift('star nosed mole', 2);
  # 'stor nesad mole'
```

```py
vowel_shift('funnily enough', 4);
  # 'finnely onuugh'
```
