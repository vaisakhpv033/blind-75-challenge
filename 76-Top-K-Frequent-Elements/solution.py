class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        output = []
        for key, val in counts.items():
            output.append((val, key))

        output = sorted(output, reverse=True)
        return [output[i][1] for i in range(k)]

        