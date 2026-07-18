"""Subarray Sum Equals K — prefix sum + hash map pattern.

Pattern: running prefix sum with a count dictionary. If prefix_sum[j] -
prefix_sum[i] == k, the subarray (i, j] sums to k. So at each index, the
number of valid subarrays ending there equals how many earlier prefixes
had value (running_sum - k).

Key details learned the hard way:
- Seed {0: 1} so subarrays starting at index 0 count without a special case.
- Look up BEFORE inserting the current prefix, or k == 0 self-matches.
- Works with negatives and zeros.

Time: O(n)  Space: O(n)
"""
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    """Return the number of contiguous subarrays of nums summing to k.

    >>> subarray_sum([1, 2, 3], 3)
    2
    """
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    running_sum = 0
    results = 0
    
    for index in range(len(nums)):
        running_sum += nums[index]
        results += prefix_sums[(running_sum - k)]
        prefix_sums[running_sum] += 1

    return results