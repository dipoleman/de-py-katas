# reduce_by_steps

For this task you should try and create your own version of a `reduce` function, (have a look at the JavaScript [array method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) if you're not sure what this means).

The function `reduce_by_steps` should accept a **binary function** \*, a **list** and an **initial value**.

\*A binary function is one that accept two arguments

## Example

```py
def multiply(num1,num2):
  return num1 * num2

numbers = [5, 5]
initial_value = 1


reduce_by_steps(multiply, numbers, initial_value) # 25
```

```py
def make_sentence(str1,str2):
  return f"{str1} {str2}"

words = ['Let\'s', 'get', 'down', 'to', 'business']
initial_value = ''


reduce_by_steps(make_sentence, words, initial_value) # 'Let's get down to business'
```
