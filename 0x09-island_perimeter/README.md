# Island Perimeter

## Description
This project involves calculating the perimeter of an island represented by a grid. The grid is a rectangular matrix where:
- `0` represents water
- `1` represents land

The goal is to write a function that returns the perimeter of the island.

## Requirements
- Python 3.x

## Usage
To use the function, you need to import it and pass a grid as an argument. The grid should be a list of lists containing integers `0` and `1`.

```python
from island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

## Function Signature
```python
def island_perimeter(grid: List[List[int]]) -> int:
    pass
```

## Example
Given the following grid:
```
[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```
The perimeter of the island is `16`.

## Testing
To run tests, you can use the `unittest` framework. Create a test file and define your test cases.

```python
import unittest
from island_perimeter import island_perimeter

class TestIslandPerimeter(unittest.TestCase):
    def test_example(self):
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(island_perimeter(grid), 16)

if __name__ == '__main__':
    unittest.main()
```

## Author
- Ismailchiba

## License
This project is licensed under the MIT License.