# find_most_repeated

Create a function that looks through a flat list and returns an dictionary that describes the most repeated element or elements in the list. The dictionary will be in the format:

```py
{
  elements: ['foo'],
  repeats: 3
}
```

If the list is empty or there are no repeated elements, return:

```py
{
  elements: [],
  repeats: null
}
```

# Examples

```py
find_most_repeated([]);
  # {elements: [], repeats: null}
```

```py
find_most_repeated(['foo', 'bar', 'hello', 'world']);
  # {elements: [], repeats: null}
```

```py
find_most_repeated(['foo', 'foo', 'bar', 'hello', 'world']);
  # {elements: ['foo'], repeats: 2}
```

```py
find_most_repeated(['foo', 'foo', 1, 2, 3, 'bar', 2, 3, 4, 'bar', 'bar', 'foo']);
  # {elements: ['foo', 'bar'], repeats: 3}
```
