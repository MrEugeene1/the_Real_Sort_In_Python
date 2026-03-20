# Bubble Sort in Python (Descending Version)

A clean and intuitive implementation of Bubble Sort that arranges numbers in descending order (largest to smallest).

## Overview

This project demonstrates:
- Interactive input from the console
- Manual sorting logic (Bubble Sort)
- Descending-order arrangement
- Basic swap counting during sorting

It is perfect for students and early developers who want to deeply understand how sorting works step by step.

## Ascending vs Descending (Core Idea)

Your first version (ascending) uses this condition:

```python
if my_list[i] > my_list[i + 1]:
```

Your second version (descending) uses:

```python
if my_list[i] < my_list[i + 1]:
```

That single operator change (`>` to `<`) flips the sorting direction.

## Project Structure

```
.
|-- bubbleSort.py
|-- README.md
```

## Requirements

- Python 3.x

## Run

From the project folder:

```bash
py bubbleSort.py
```

## Example Run (Descending)

```text
How many elements do you want to sort: 6
Enter a list element: 4
Enter a list element: 7
Enter a list element: 1
Enter a list element: 9
Enter a list element: 3
Enter a list element: 6

Sorted:
[9.0, 7.0, 6.0, 4.0, 3.0, 1.0]
9 comparisons
```

## How the Algorithm Works

1. Read the number of values.
2. Collect each value into a list.
3. Keep looping while swaps are happening.
4. Compare neighboring elements.
5. Swap them when left is smaller than right (for descending order).
6. Stop when no swaps occur in a full pass.

## Complexity

- Best case: O(n) (already in descending order, early stop)
- Average case: O(n^2)
- Worst case: O(n^2)
- Space complexity: O(1) extra space

## Important Note About the Counter

In this script, `counter` is increased when a swap happens.

So the output label "comparisons" is not technically accurate.

More accurate labels would be:
- `swaps`
- `swap operations`

## Professional Improvements You Can Add

- Rename the final print to `swaps` for correctness.
- Add input validation with `try/except`.
- Move logic into reusable functions for testability.
- Add optional mode selection (`ascending` or `descending`).
- Add unit tests for duplicates, negatives, and decimal values.

## License

Educational and personal use.
# Bubble_Sort_With_Python_2
# Bubble_Sort_With_Python_2
