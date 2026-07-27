"""Longest Substring Without Repeating Characters — sliding window.

Pattern: a window [start, i] holding only unique chars. A dict maps each
char to its last-seen index. When we hit a char already in the window,
jump start past its previous occurrence.

The one trap (this is the whole problem):
    start = max(start, letters[c] + 1)
The max is load-bearing. Without it, a repeat whose stored index sits
BEHIND the current start rewinds the window and re-admits already-evicted
characters. Canonical failing case: "abba" — when the second 'a' appears,
its old index (0) is behind start (2); a naive `start = old + 1` moves the
window backwards. A window boundary must be monotonic: it only moves forward.

Time: O(n) — each index enters/leaves the window once.
Space: O(min(n, k)) where k is the alphabet size.
"""

def longest_substring(s : str) -> int:
    """Longest Substring Without Repeating Characters. Given a string s, find the length of the longest
    substring with no repeating characters.
    Example: "abcabcbb" → 3 (the answer is "abc"). "bbbbb" → 1 ("b"). "pwwkew" → 3 ("wke")."""
    longest = 0
    letters = {}

    start = 0
    for i in range(len(s)):
        if s[i] in letters:
            start = max(start, letters[s[i]] + 1)

        letters[s[i]] = i
        length = i - start + 1
        longest = max (length, longest)

    return longest

