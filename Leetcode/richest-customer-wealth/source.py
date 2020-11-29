class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for account in accounts:
            max_value = max(max_value, sum(account))

        return max_value
