import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # count the frequency of each card
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0) + 1

        # create a min-heap of the unique cards
        minH = list(count.keys())
        heapq.heapify(minH)

        # try to create group starting from the smallest card
        while minH:
            first = minH[0]
            #try to form a group startinng with 'first
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

sol = Solution()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(sol.isNStraightHand(hand, groupSize)) # Output will be True

hand2 = [1, 2, 3, 4, 5]
groupSize2 = 4
print(sol.isNStraightHand(hand2, groupSize2))  # Output will be False