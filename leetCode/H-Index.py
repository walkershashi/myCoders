class Solution:
    def hIndex(self, citations: List[int]) -> int:
        bucket = [0] * (len(citations) + 1)
        
        for i in range(len(citations)):
            if citations[i] > len(citations):
                bucket[len(citations)] += 1
            else:
                bucket[citations[i]] += 1
        
        count = 0
        for i in range(len(bucket) - 1, -1, -1):
            count += bucket[i]
            
            if count >= i:
                return i
