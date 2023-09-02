# find_partner

1. An list containing lists of students
2. An list of directions.

You need to return an list of all of the students you have moved over.

For example. Our student dataset shows the current seating plan.

```py
students = [
  ['Joe',  'David', 'Alex', 'Duncan', 'Cat', 'Verity'],
  ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan']
];
```

Rules:

1. This list allows you to loop horizontally but not vertically. i.e. if you are at the leftmost item and go left again it will take you to the rightmost item in the same list. However, if you at the top of the list and try to go up, you will stay where you are.

2. You can assume you always start at position `[0, 0]` (top left corner) and that you don't need to add the starting person to the results.

3. Directions will be either;
   `up, down, left, right`

4. If you go up/down and you cannot move, then do not add that person on to the list again.

## Examples

```py
traverseStudents(students, ['right'])
  # ['David']
```

```py
traverseStudents(students, ['left'])
  # ['Verity']
```

```py
traverseStudents(students, ['right', 'right', 'right'])
  # ['David', 'Alex', 'Duncan']
```

```py
traverseStudents(students, ['right', 'up', 'up'])
  # ['David']
```
