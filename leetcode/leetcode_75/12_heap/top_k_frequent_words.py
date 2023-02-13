import heapq
from collections import Counter
from typing import List


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

    def __repr__(self):
        return f"({self.word}, {self.freq})"


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)

        print(f"Words counter: {cnt}.")
        h = []
        for word, freq in cnt.items():
            print(f"\nAdd word: {word}, freq: {freq} to heap.")
            heapq.heappush(h, Pair(word, freq))
            print(f"Heap now: {h}.")

            if len(h) > k:
                popped_item = heapq.heappop(h)
                print(f"Removing {popped_item} from heap.")
        return [p.word for p in sorted(h, reverse=True)]


sol = Solution()
print(
    f'\nOutput: {sol.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2)}.'
)

"""
Output:
Words counter: Counter({'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1}).

Add word: i, freq: 2 to heap.
Heap now: [(i, 2)].

Add word: love, freq: 2 to heap.
Heap now: [(love, 2), (i, 2)].

Add word: leetcode, freq: 1 to heap.
Heap now: [(leetcode, 1), (i, 2), (love, 2)].
Removing (leetcode, 1) from heap.

Add word: coding, freq: 1 to heap.
Heap now: [(coding, 1), (i, 2), (love, 2)].
Removing (coding, 1) from heap.
Output: ['i', 'love'].

Time Complexity: O(nlogk), where N is the length of words. We count the frequency of each word in O(N) time, 
then we add N words to the heap, each in O(logk) time. 
Finally, we pop from the heap up to kkk times or just sort all elements in the heap as the returned result, 
which takes O(klogk). As k≤N  O(N)+O(Nlogk)=O(Nlogk)

Space Complexity: O(n)
"""
