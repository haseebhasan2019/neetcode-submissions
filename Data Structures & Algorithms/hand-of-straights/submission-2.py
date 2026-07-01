class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        card_freq = Counter(hand) # card -> freq
        for card in sorted(card_freq):
            freq = card_freq[card]
            if freq == 0: # card handled
                continue
            for i in range(groupSize):
                if card_freq[card+i] < freq:
                    return False
                card_freq[card+i] -= freq
        return True