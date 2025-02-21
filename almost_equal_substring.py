# Problem source: https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/


# Note: will return -1 as described in the problem description
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        assert s.isalpha() and s.islower()
        assert pattern.isalpha() and pattern.islower()
        # Sanity check
        assert len(pattern) <= len(s)
        assert len(pattern) != 0
        # Additional constraints introduced by the task description
        assert len(s) <= 10**5

        # Iterate through possible candidate substrings
        for i in range(len(s) - len(pattern) + 1):
            # Initialize "at most one disagreement" flag
            altered_character_found = False
            continue_outer_loop = False
            # Iterate through the pattern string
            for j in range(len(pattern)):
                if s[i+j] != pattern[j]:
                    if altered_character_found:
                        continue_outer_loop = True
                        break
                    else:
                        altered_character_found = True

            if continue_outer_loop:
                continue
            else:
                return int(i)
        # If have exited the loop - that means no solution has been found
        return -1

