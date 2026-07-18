"""Remove Duplicates from Sorted Array — two-pointer (reader/writer) pattern.

Pattern: slow pointer i marks the end of the deduplicated prefix; fast
pointer j scans. When nums[j] differs from nums[i], advance i and write.

Key details learned the hard way:
- Guard the empty case once up front; then `i + 1` is always the answer.
  Maintaining a separate count variable that shadows i invites stale-value
  bugs at loop exit (an all-unique array exposed exactly that).
- Test inputs that end in ways the loop doesn't expect: all-unique,
  unique-at-the-end, not just all-duplicates.

Time: O(n)  Space: O(1)
"""
def remove_duplicates(nums: list[int]) -> int:
    """Dedupe sorted nums in place; return count of unique elements.

    The first u slots of nums hold the unique values afterward.

    >>> a = [1, 1, 2, 3, 3]
    >>> remove_duplicates(a), a[:3]
    (3, [1, 2, 3])
    """
    
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1

if __name__ == "__main__":
    print(remove_duplicates([1,1,2,3,3]))
    print(remove_duplicates([1,2,3]))
    print(remove_duplicates([]))
    print(remove_duplicates([2, 2, 2, 2]))
    print(remove_duplicates([3]))