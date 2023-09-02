# Digital Root

The **digital root** of a number is the _recursive sum of all the digits in the number_.

Function should take a number and calculate the sum of the digits. If that value has more than one digits you should continue reducing it in the same way until a single digit number is produced.

## Examples:

```py
digital_root(16)
# 1 + 6 = 7
digital_root(942
# 9 + 4 + 2 = 15 -> 1 + 5 = 6
digital_root(132189)
# 1 + 3 + 2 + 1 + 8 + 9 = 24
# 2 + 4 = 6
digital_root(493193)
# 4 + 9 + 3 + 1 + 9 + 3 = 29
# 2 + 9 = 11
# 1 + 1 = 2
```
