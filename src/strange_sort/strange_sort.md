# Strange Sort

Your task is to create a function which takes an arbitrary number of string arguments and returns a list of them sorted by their length rather than alphabetical order. However, if there are words of identical length, they should be sorted in alphabetical order within the list.

The default should be to sort in descending length order, but this should be configurable. The list should be passed in as an arbitrary number of arguments rather than a list object. The sorting should be case insensitive.

Examples
```python
strange_sort('big', 'enormous', 'small')
# returns ['enormous', 'small', 'big']

strange_sort('big', 'enormous', 'small', descending=False)
# returns ['big', 'small', 'enormous']

strange_sort('three', 'big', 'nasty', 'bad', 'expressions')
# returns ['expressions', 'nasty', 'three', 'bad', 'big']

strange_sort('three', 'Big', 'nasty', 'bad', 'expressions')
# returns ['expressions', 'nasty', 'three', 'bad', 'Big']
```

