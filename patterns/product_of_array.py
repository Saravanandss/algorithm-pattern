"""
Product of Array Except Self. Given an integer array nums, return an array output where output[i] is the product of all
elements of nums except nums[i].
Constraints: Not use division.
Example: nums = [1,2,3,4] → [24,12,8,6]. (For index 0: 2·3·4=24. For index 1: 1·3·4=12. Etc.)
product_of_array version time / space complexity O(n) / O(n)
product_of_array_v2 version time / space complexity O(n) / O(1)
"""

def product_of_array(nums):
    """
        First draft — correct but over-engineered. Kept as a learning record.

        Allocates two separate (n+1)-length prefix/suffix arrays AND branches on
        i==0 / i==n-1 in the combine step. Both are unnecessary: the preferred
        version shows the same result needs no auxiliary arrays and no
        boundary special-casing.

        Time: O(n). Space: O(n).
        >>>product_of_array([1,2,3,4])
        [24,12,8,6]
    """
    n = len(nums)

    prefix_product = [1] * (n + 1)
    suffix_product = [1] * (n + 1)
    output = [1] * n

    # seed
    prefix_product[-1] = 1
    suffix_product[n] = 1

    for i in range(n):
        prefix_product[i] = prefix_product[i-1] * nums[i]

    for i in range(n-1, -1, -1):
        suffix_product[i] = suffix_product[i + 1] * nums[i]

    for i in range(n):
        if i == 0:
            output[i] = suffix_product[i+1]
        elif i == n - 1:
            output[i] = prefix_product[i-1]
        else:
            output[i] = prefix_product[i-1] * suffix_product[i+1]

    return output

def product_of_array_v2(nums):
    """Space-optimized to O(1) extra: prefix pass into output, then a single
    rolling `suffix` scalar carries the right-side product backward.
    Time: O(n). Space: O(1) extra.
    """
    n = len(nums)
    output = [1] * n

    for i in range(n):
        output[i] = (output[i - 1] if i > 0 else 1) * nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] = (output[i-1] if i > 0 else 1) * suffix
        suffix *= nums[i]

    return output