"""Find the Kth Largest Element — three approaches on the selection-problem ladder.

Given an unsorted array and k, return the k-th largest element in sorted
order (positional, NOT k-th distinct: for [5,5,4], the 2nd largest is 5).

Assuming: valid domain is a non-empty array with 1 <= k <= len(nums).
Anything else raises ValueError rather than returning a sentinel, because
any sentinel (-1, None, 0) can collide with a legitimate array value.

The escalation ladder, weakest to strongest:
  - Sort then index: O(n log n). The anchor — always mention, never submit.
  - Size-k min-heap (v2): O(n log k) time, O(k) space. PREFERRED. Doesn't
    mutate input; wins when k << n; uses only the public heapq API.
  - Max-heapify + pop k (v1): O(n + k log n), O(1) space but DESTROYS input.
    Wins when k approaches n. Requires Python 3.14+ (heapify_max is public
    only from 3.14; on <=3.13 it's the private heapq._heapify_max).
  - Quickselect (v3): O(n) average, O(1) space. Fastest on
    average; worst case hits already-sorted input unless the pivot is
    randomized.

The key inversion worth remembering: to track the k LARGEST values you keep
a MIN-heap of size k. The root is the weakest of your current top-k, so it's
both the one to evict when a bigger value arrives and, after the full pass,
the answer itself.
"""
import heapq


def find_kth_largest_max_heap(nums: list[int], k: int) -> int:
    """Max-heapify the whole array, pop k times. Requires Python 3.14+.
    Time: O(n + k log n)   Space: O(1)   Input: DESTROYED.
    """
    if not nums or not (1 <= k <= len(nums)):
        raise ValueError("Input array must not empty and it's length must be greater than or equal to k")

    # Takes O(n) time
    heapq.heapify_max(nums)

    kth_largest: int = 0
    for _ in range(k):
        kth_largest = heapq.heappop_max(nums)

    return kth_largest


def find_kth_largest_min_heap(nums: list[int], k: int) -> int:
    """PREFERRED. Size-k min-heap; root is the k-th largest after one pass.

    Fill the heap to size k, then for each further element replace the root
    only if the newcomer beats it. heapreplace = pop-min + push in one
    O(log k) op.

    Time: O(n log k)   Space: O(k)   Input: not mutated.
    """
    if not nums or not (1 <= k <= len(nums)):
        raise ValueError("Input array must not empty and it's length must be greater than or equal to k")

    h: list[int] = []

    for n in nums:
        if len(h) < k:
            heapq.heappush(h, n)
        elif n > h[0]:
            heapq.heapreplace(h, n)
    return h[0]


def find_kth_largest_quickselect(nums: list[int], k: int) -> int:
    """Quickselect: partition around a pivot; recurse only into the side
        holding the target index. k-th largest maps to index (n - k) in ascending
        order.
        Time: O(n) average, O(n^2) worst (on already sorted array)   Space: O(1)   Input: reordered.
        """
    if not nums or not (1 <= k <= len(nums)):
        raise ValueError("Input array must not empty and it's length must be greater than or equal to k")

    start, end = 0, len(nums) - 1
    x = partition(nums, start, end)
    desired_x = len(nums) - k

    while x != desired_x:
        if x > desired_x:
            end = x - 1
        else:
            start = x + 1
        x = partition(nums, start, end)

    return nums[x]

def partition(nums: list[int], start: int, end: int) -> int:
    pivot = nums[end]
    i = start - 1

    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1