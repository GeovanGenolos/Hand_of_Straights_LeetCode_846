# This is my code in solving LeetCode 846: Hand of Straights

## The solution involves several key steps:

- Initial Check: Verify if the total number of cards is divisible by groupSize. If not, return False immediately.

- Frequency Count: Use a dictionary to count the frequency of each card.

- Min-Heap Creation: Create a min-heap from the unique card values to always get the smallest available card.

- Group Formation: Attempt to form consecutive groups starting from the smallest card available in the heap.

```
import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # Create a min-heap of the unique cards
        minH = list(count.keys())
        heapq.heapify(minH)
        
        # Try to create groups starting from the smallest card
        while minH:
            first = minH[0]
            # Try to form a group starting with 'first'
            for i in range(first, first + groupSize):
                if i not in count or count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True

# Example usage
sol = Solution()

# Example 1
hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize1 = 3
print(sol.isNStraightHand(hand1, groupSize1))  # Output: True

# Example 2
hand2 = [1, 2, 3, 4, 5]
groupSize2 = 4
print(sol.isNStraightHand(hand2, groupSize2))  # Output: False
```

## Imports:

- 'heapq' for heap operations.
- 'List' from 'typing' for type hinting.
  
## Method isNStraightHand:

- Initial Check: 'if len(hand) % groupSize != 0: return False'
- Checks if the number of cards is divisible by 'groupSize'.

- Frequency Count:
```
count = {}
for n in hand:
    count[n] = 1 + count.get(n, 0)
```
- Counts the frequency of each card in hand.

- Min-Heap Creation:
```
minH = list(count.keys())
heapq.heapify(minH)
```
- Creates a min-heap from the unique card values to always access the smallest card.

- Group Formation:
```
while minH:
    first = minH[0]
    for i in range(first, first + groupSize):
        if i not in count or count[i] == 0:
            return False
        count[i] -= 1
        if count[i] == 0:
            if i != minH[0]:
                return False
            heapq.heappop(minH)
```
- Continues to form groups starting from the smallest card.
- For each card in the range from first to first + groupSize - 1, it checks if the card is available in the required quantity.
- Decreases the count of each card used and removes it from the heap if its count reaches zero.
