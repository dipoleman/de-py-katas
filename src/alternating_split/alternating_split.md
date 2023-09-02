# Alternating Split Encryption

Implement a simple encryption algorithm which is given a string `S` and an integer `N`.

Your function should concatenate all odd-indexed characters of `S` with all the even-indexed characters of `S`, this process should be repeated `N` times.

## Examples:

```py
encrypt("012345", 1) # "135024"
encrypt("012345", 2) # "135024"  ->  "304152"
encrypt("012345", 3) # "135024"  ->  "304152"  ->  "012345"
```

## Extension

Create a decryption function that reverses the above process.
