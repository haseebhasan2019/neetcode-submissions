class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        card_freq = Counter(hand) # card -> freq
        for card in hand:
            if card not in card_freq: # card handled
                continue
            if card-1 not in card_freq: # start of a straight
                curr_size = 0
                next_card = card
                while next_card in card_freq:
                    # decrement count
                    if card_freq[next_card] == 1:
                        del card_freq[next_card]
                    else:
                        card_freq[next_card] -=1
                    # increment size
                    curr_size+=1
                    if curr_size == groupSize:
                        break
                    next_card+=1
                if curr_size != groupSize:
                    return False
        return not card_freq