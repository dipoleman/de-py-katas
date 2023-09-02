# calculate_binary_score

Given an list of even and odd positive numbers, you need to work out if each number is odd or even.

If it is odd, you need to convert it to binary code and count how many 1's there are. If the number is even, you need to convert it to binary code and count how many are 0's there are.

You need to keep track of the odd number scores for 1s and the even number scores for 0s and after getting the final scores, you need to return which team won by either returning:

```py
"odds win"
```

```py
"evens win"
```

or

```py
"tie"
```

---

For example with an list of [2, 3]:

`2` is even and `2` converted to binary is `10` so the score for even numbers (based on the number of `0`s in the binary) is 1.

`3` is odd and `3` converted to binary is `11` so the score for even numbers (based on the number of `1`s in the binary) is 2.

Therefore calculate_binary_score would return `odds win`

---

## Examples

```
calculate_binary_score([1])
  # 'odds win'
```

```
calculate_binary_score([1, 2])
  # 'tie'
```

```
calculate_binary_score([1, 2, 3, 4, 5])
  # 'odds win'
```

```
calculate_binary_score([1, 20])
  # 'evens win'
```
