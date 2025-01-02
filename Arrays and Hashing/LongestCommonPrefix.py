# A bit diifficult for me need to rmb the edgecases
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        return prefix
