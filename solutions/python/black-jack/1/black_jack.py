"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    face_cards = 'JQK'
    ace_card = 'A'

    if card in face_cards:
        return 10
    if card == ace_card:
        return 1

    return int(card)
    pass


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    face_cards = 'JQK'
    ace_card = 'A'

    if card_one in face_cards:
        number_one = 10
    elif card_one == ace_card:
        number_one = 1
    else:
        number_one = int(card_one)

    if card_two in face_cards:
        number_two = 10
    elif card_two == ace_card:
        number_two = 1
    else:
        number_two = int(card_two)

    if number_one > number_two:
        return card_one
    elif number_one < number_two:
        return card_two
    else:
        return card_one, card_two
    
    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    result_one = 0
    result_two = 0
    
    if card_one == 'A' or card_two == 'A':
        return 1
        
    if card_one in 'JQK':
        result_one = 10
    else:
        result_one = int(card_one)
        
    if card_two in 'JQK':
        result_two = 10
    else:
        result_two = int(card_two)

    total = result_one + result_two

    if total > 10:
        return 1
    else:
        return 11

    pass


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if (card_one in 'JQK' or card_one == '10') and card_two == 'A':
        return True
    if (card_two in 'JQK' or card_two == '10') and card_one == 'A':
        return True
    return False
    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if card_one == card_two:
        return True
    if card_one in 'JQK' and card_two in 'JQK':
        return True
    return False
    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    # 1. Define a helper or logic to get the value of a card
    def get_value(card):
        if card in 'JQK':
            return 10
        if card == 'A':
            return 1
        return int(card)

    # 2. Calculate the total
    total = get_value(card_one) + get_value(card_two)

    # 3. Return True if total is 9, 10, or 11, otherwise False
    return total in [9, 10, 11]
