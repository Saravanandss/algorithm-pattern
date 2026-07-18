# Coding Patterns

Working solutions to classic problems, one per algorithmic
pattern, each annotated with the mistakes made on the way to the final
version. The bugs are documented deliberately.

## Patterns covered

| Problem | Pattern | Time / Space | Trap documented |
|---|---|---|---|
| [Subarray Sum Equals K](patterns/subarray_sum.py) | Prefix sum + hash map | O(n) / O(n) | Insert-before-lookup self-match when k = 0 |
| [Remove Duplicates (sorted, in-place)](patterns/remove_duplicates.py) | Two pointers (reader/writer) | O(n) / O(1) | Shadow count variable going stale at loop exit |
| [Valid Palindrome](patterns/is_palindrome.py) | Two pointers (converging, with skip) | O(n) / O(1) | Unbounded skip loop walking off the string |

## Running the tests

```bash
pip install pytest
python -m pytest tests/ -v
```

All suites include the adversarial cases that broke earlier drafts.

## Structure

```
.
├── patterns/          # one file per problem, final version + lessons
├── tests/             # pytest suites, parametrized
└── README.md
```
