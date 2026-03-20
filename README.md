# Python Sort Method Demo

Professional, beginner-friendly demonstration of sorting numeric input using Python's built-in `list.sort()` method.

## Overview

This small tool reads numbers from user input, stores them in a list, and sorts them in ascending order with Python's native sorting engine.

It is ideal for:
- Learning how `list.sort()` works in practice
- Understanding input-to-output data flow in a console app
- Comparing built-in sorting against manual algorithms (like Bubble Sort)

## Why `list.sort()`

Python's built-in sort is:
- Fast and production-ready
- In-place (modifies the existing list)
- Stable (preserves order of equal elements)
- Suitable for most real-world sorting tasks

## Project Files

```
.
|-- theSort.py
|-- README.md
```

## Requirements

- Python 3.8+

## Run the Program

From the project folder:

```bash
py theSort.py
```

## Example Execution

```text
How many elements do you want to sort: 5
Enter a list element: 8
Enter a list element: 1
Enter a list element: 3
Enter a list element: 2
Enter a list element: 9

Sorted:
[1.0, 2.0, 3.0, 8.0, 9.0]
1 comparisons
```

## How It Works

1. Ask for total number of elements.
2. Read each numeric input (`float`).
3. Append values to a list.
4. Call `my_list.sort()`.
5. Print sorted output.

## Complexity Notes

Python uses Timsort internally for `list.sort()`.

- Time: O(n log n) average and worst case
- Best case: can approach O(n) on partially ordered data
- Space: efficient in practice, implementation-managed

## Important Note About Counter

In the current script, `counter` is incremented once before sorting and printed as "comparisons".

This means:
- It is not counting actual comparisons.
- It currently behaves as a placeholder value.

If you want, this can be replaced with meaningful metrics (e.g., number of elements, elapsed time, or custom comparison tracking using another approach).

## Possible Improvements

- Add input validation (`try/except`) to handle invalid numbers.
- Support descending sorting via `my_list.sort(reverse=True)`.
- Wrap logic in functions for cleaner structure and easier testing.
- Add unit tests for empty input, duplicates, negatives, and decimal values.

## License

For educational and personal use.

