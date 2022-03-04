table_cards = ["A_S", "J_H", "7_D", "8_S", "10_D"]
hand_cards = ["J_D", "3_D"]

suits_table = [x[-1] for x in table_cards]
suits_hand = [i[-1] for i in hand_cards]

suits = suits_table + suits_hand

flush = any([suits.count(val) >= 5 for val in suits])

if flush:
    print('Flush!')
else:
    print('No Flush!')






