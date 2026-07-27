"""
Climbing Stairs: You're climbing a staircase with n steps. Each time you can climb either 1 or 2 steps. In how many distinct ways can you reach the top?
Example: n = 3 → 3 (the ways are 1+1+1, 1+2, 2+1).

Key details learned the hard way:
- it can be built from the base up. 
    We calculate how many ways to climb a stair, keep its answer aside. With an additional step, we can either go one or two steps up (1+1, or 2).
    With introduction of each step, we can either add one step to the last answer (i-1), or two steps from its predecessor (i-2).
    So at any iteration, we can do f(i) = f(i-1) + f(i+1). This resembles fibonacci sequence.
- Base cases and seed values need to be selected carefully

    Time: O(n) Space:O(1)
"""
def climbing_stairs(n: int) -> int:
    if n <= 0:
        return 0
    
    a, b = 0, 1

    for i in range(n+1):
        b, a = a, a + b

    return a