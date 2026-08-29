class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        di = Counter(tasks)
        m = max(di.values())
        mcount = sum(v == m for v in di.values())
        return max(len(tasks), mcount + (n + 1) * (m - 1))