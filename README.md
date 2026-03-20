# Python sort() Method Demo

A clean, professional example showing how to sort user-provided numbers using Python's built-in list sorting method.

## Overview

This project demonstrates a practical console workflow:
1. Ask the user how many elements to sort.
2. Read each element as a number.
3. Store values in a Python list.
4. Sort the list using `my_list.sort()`.
5. Print the final sorted result.

It is simple, intuitive, and ideal for learning Python fundamentals.

## Why Use sort()

Python's `list.sort()` is the preferred method in most real applications because it is:
- Efficient
- Stable (keeps original order of equal elements)
- In-place (modifies the existing list without creating a new one)
- Easy to use and highly reliable

## Project Structure

```
.
|-- bubbleSort.py
|-- README.md
```

## Requirements

- Python 3.x

## Run the Program

Open a terminal in the project folder and run:

```bash
py bubbleSort.py
```

## Example Output

```text
How many elements do you want to sort: 5
Enter a list element: 8
Enter a list element: 3
Enter a list element: 7
Enter a list element: 1
Enter a list element: 4

Sorted:
[1.0, 3.0, 4.0, 7.0, 8.0]
1 comparisons
```

## Complexity

Python uses Timsort internally for `sort()`.

- Best case: O(n)
- Average case: O(n log n)
- Worst case: O(n log n)
- Extra space: efficient and implementation-managed

## Notes About Current Counter

In the current script, `counter` is incremented once and printed as "comparisons".

This does not represent real comparison count. It is currently a placeholder metric.

If you want an accurate metric, use one of the following:
- Rename it to `operations` or `runs`
- Measure elapsed time
- Implement manual comparison counting in a custom sorting algorithm

## Useful sort() Variations

- Descending order:

```python
my_list.sort(reverse=True)
```

- Sort without modifying original list:

```python
sorted_list = sorted(my_list)
```

## Suggested Improvements

- Add input validation using `try/except`.
- Refactor into functions for cleaner design and easier testing.
- Add unit tests for edge cases (empty input, duplicates, negatives, decimals).

## License

For educational and personal use.
