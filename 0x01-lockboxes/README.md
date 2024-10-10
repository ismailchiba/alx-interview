
# 0. Lockboxes

## Description

You are given `n` number of locked boxes, numbered sequentially from `0` to `n - 1`. Each box may contain keys to other boxes, and your task is to determine if all the boxes can be unlocked.

## Task

Write a method that determines if all the boxes can be opened.

### Prototype

```python
def canUnlockAll(boxes)
```

- `boxes`: A list of lists, where each list represents a box and contains keys (positive integers) to other boxes.
- The first box `boxes[0]` is always unlocked.
- A key with the same number as a box can open that box.
- There may be keys that do not correspond to any box.
- Return `True` if all boxes can be opened, else return `False`.

### Requirements

- You need to determine if all the boxes can be unlocked by starting with the first box and using the keys found within it.
  
## Example

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes)) # True
```

### Explanation:
- Box 0 contains key 1.
- Box 1 contains key 2.
- Box 2 contains key 3.
- Box 3 contains key 4.
- Box 4 contains no keys, but all boxes have been opened.

### Edge Case:

```python
boxes = [[1, 3], [2], [1], []]
print(canUnlockAll(boxes)) # True
```

### Another Example:

```python
boxes = [[1, 2], [], [3], []]
print(canUnlockAll(boxes)) # False
```

## Testing

You can write unit tests to validate the function with various test cases, including edge cases where some boxes cannot be unlocked.
