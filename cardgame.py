import random as rnd

deck = []

suits = ("черви", "буби", "пики", "крести")
def make_deck():
    # колода
    for suit in suits:
        for i in range(6, 15):
            card = {}
            card["масть"] = suit
            card["цена"] = i 
            deck.append(card)

    # перемешивание колоды
    rnd.shuffle(deck)


def make_table():
    # создание стола
    table = []
def make_hands():
    # создание рук c раздачей карт
    user_hand = deck[:18]
    computer_hand = deck[18:]


def new_round(user_hand, computer_hand, table):
    while user_hand and computer_hand:
        # делаем ход
        table.append(user_hand.pop())
        table.append(computer_hand.pop())

        # сравнием карты
        user_card = table[-2]["цена"]
        computer_card = table[-1]["цена"]

        print("игрок выкинул", user_card)
        print("")

        if user_card > computer_card:
            print("win")
            user_hand = table + user_hand
            print(user_hand)
            table.clear()
        elif user_card < computer_card:
            print("loss")
            computer_hand = table + computer_hand
            print(user_hand)
            table.clear()
        else:
            print("continuation")
            new_round()
    if user_hand == True:
        print("Ты выйграл!")
    elif computer_hand == True:
        print("Ты проиграл!")



def new_game():
    make_deck()
    make_table()
    make_hands()
    new_round(user_hand, computer_hand, table)


new_game() #fixme ошибка про user_hand; user_hand не найден в new_round