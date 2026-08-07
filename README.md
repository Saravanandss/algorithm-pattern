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
| [Longest Substring Without Repeats](patterns/longest_substring.py) | Sliding window | O(n) / O(min(n, k)) | Window start jumping backwards on a stale index ("abba") — boundaries must be monotonic |
| [Product of Array Except Self](patterns/product_of_array.py) | Prefix/suffix sweep | O(n) / O(1) extra | Length-1 must return [1] (empty product), not the input; zeros handled free vs. the division approach |
| [Kth Largest Element](patterns/kth_largest_element.py) | Size-k min-heap · max-heap · quickselect | O(n log k) / O(k) | Min-heap inversion for "largest"; sentinel-seeded heap; fixed pivot degrading to O(n²) on sorted input |
| [Climbing Stairs](dp/climbing_stairs.py) | 1D dynamic programming | O(n) / O(1) | "Sum over possible last moves" is the transferable method — {1,2} steps makes it Fibonacci incidentally; {1,2,3} would give f(n) = f(n−1) + f(n−2) + f(n−3) |
| [Number of Islands](graphs/count_islands.py) | Connected components — union-find & flood fill | O(m·n) / O(m·n) | Non-injective string keys (f"{i}{j}") colliding on grids wider than 10; list-of-sets union costing O(n²) |
| [Shortest Clear Path](graphs/clear_path.py) | BFS on an implicit grid graph | O(n²) / O(n²) | BFS's ring-order guarantee vs. DFS ("probably faster" is the wrong claim — it's *correctness*, not speed) |
| [Universal Sink](graphs/universal_sink.py) | Matrix two-pointer elimination | O(n) / O(1) | A "graph" problem that never traverses — elimination-then-verify; classify by technique, not by story |

## Running the tests

```bash
pip install pytest
python -m pytest tests/ -v
```

All suites include the adversarial cases that broke earlier drafts.

## Structure

```
.
├── dp/                # dynamic programming
├── graphs/            # traversal, components, grid-as-graph
├── patterns/          # arrays, strings, heaps, windows
├── tests/             # mirrors the source tree
└── README.md
```