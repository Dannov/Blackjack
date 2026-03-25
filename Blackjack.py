import random
import time

# check pygame

# do one dealer card secret as in the real game
# optimize
# fix minor bugs
# fix logic

print(f'welcome to black jack')
time.sleep(1)

def deck_refresh():
    return  {"2 ♡" : 2,"3 ♡" : 3,"4 ♡" : 4,"5 ♡" : 5,"6 ♡" : 6, "7 ♡" : 7, "8 ♡" : 8, "9 ♡" : 9, "10 ♡" : 10, "Jack ♡" : 10, "Queen ♡" : 10, "King ♡" : 10, "Ace ♡" : 11,
             "2 ♢" : 2,"3 ♢" : 3,"4 ♢" : 4,"5 ♢" : 5,"6 ♢" : 6, "7 ♢" : 7, "8 ♢" : 8, "9 ♢" : 9, "10 ♢" : 10, "Jack ♢" : 10, "Queen ♢" : 10, "King ♢" : 10, "Ace ♢" : 11,
             "2 ♧" : 2,"3 ♧" : 3,"4 ♧" : 4,"5 ♧" : 5,"6 ♧" : 6, "7 ♧" : 7, "8 ♧" : 8, "9 ♧" : 9, "10 ♧" : 10, "Jack ♧" : 10, "Queen ♧" : 10, "King ♧" : 10, "Ace ♧" : 11,
             "2 ♤" : 2,"3 ♤" : 3,"4 ♤" : 4,"5 ♤" : 5,"6 ♤" : 6, "7 ♤" : 7, "8 ♤" : 8, "9 ♤" : 9, "10 ♤" : 10, "Jack ♤" : 10, "Queen ♤" : 10, "King ♤" : 10, "Ace ♤" : 11}

def hand_refresh():
    return []

def draw_card(deck):
    card = random.choice(list(deck.keys()))
    point = deck[card]
    print(card)
    time.sleep(1)
    del deck[card]
    return point

def dealer_turn(deck):
    check_dealer = hand_refresh()
    print("dealer cards are")
    time.sleep(1)
    card1 = draw_card(deck)
    card2 = draw_card(deck)
    check_dealer.extend([card1 , card2])
    all_points = card1 + card2
    print(f"dealer cards whole value = {all_points}")
    return all_points, check_dealer

def player_turn(deck):
    check_player = hand_refresh()
    print("your cards are")
    time.sleep(1)
    card1 = draw_card(deck)
    card2 = draw_card(deck)
    check_player.extend([card1 , card2])
    all_points = card1 + card2
    print(f"your cards whole value = {all_points}")
    time.sleep(1)
    return all_points , check_player

def hit(deck):
    card3 = draw_card(deck)
    value = card3
    return value

def check_ace_dealer(dealer_hand, all_points):
    for card in dealer_hand:
        if card == 11 and all_points > 21:
            all_points -= 10
            print(f'because dealer has Ace and his value > 21 his new value is {all_points}')
            time.sleep(1)
    print('checked dealer hand')
    return all_points

def check_ace_player(player_hand , all_points):
    for _ in player_hand:
        if _ == 11 and all_points > 21:
            all_points -= 10
            print(f'because you have Ace and your value > 21 your new value is {all_points}')
            return all_points
    print('checked player hand')
    return all_points

def check_game(player_cards , dealer_cards):
    if player_cards > 21:
        return 'l'
    elif dealer_cards > 21:
        return 'w'
    elif player_cards > dealer_cards:
        return 'w'
    elif player_cards < dealer_cards:
        return 'l'
    elif player_cards == dealer_cards:
        return 'd'
    else:
        print("something went wrong in 'check_game()'")

def play_again():
    answer2 = None
    while answer2 not in ('yes' , 'y' , 'no' , 'n'):
        answer2 = str(input('do you want to play again? yes/no\n: '))
        if answer2 == 'yes' or answer2 == 'y':
            print('shuffling cards please wait...')
            time.sleep(3)
            return 'y'
        elif answer2 == 'no' or answer2 == 'n':
            print('round has ended')
            return 'n'

def menu_black():
    while True :
        answer = str(input("""/check_balance\n/add_funds\n/payout\n/start_game\n/end\n: """)).lower().strip()
        if answer in ('check_balance' , '/check_balance' , 'check balance' , '/check balance'):
            wallet_read()
            continue
        elif answer in ('add_funds' , '/add_funds','add funds','/add funds'):
            wallet_add()
            time.sleep(1)
            continue
        elif answer in ('/payout' , 'payout'):
            wallet_payout()
            time.sleep(1)
            continue
        elif answer in ('/start_game' ,'start_game','start game','/start game' , '/start' , 'start'):
            game_main()
            time.sleep(1)
            continue
        elif answer in ('end' , '/end'):
            break

def bet_amount(balance):
    time.sleep(1)
    while True:
        try:
            bet = (int(input('how much do you want to bet?\n: ')))
        except ValueError:
            print('please enter a number')
            time.sleep(1)
            continue
        if not 0 <= bet <= balance:
            print('invalid bet amount')
            time.sleep(1)
            continue
        answer3 = str(input(f'your bet is {bet} , is that correct?\n: '))
        if answer3 in ('yes' , 'y'):
            print('let the game begin')
            time.sleep(2)
            return bet
        else:
            continue

def calculate_money(bet , result):
    if result == 'w':
        print(f'you won {bet}')
        return bet
    elif result == 'l':
        print(f'you lost {bet}')
        return -bet
    elif result == 'd':
        print('your money stays the same')
        return 0
    else:
        print("something went wrong in 'calculate_money'")

def wallet_read():
    try:
        with open('wallet.txt' , 'r') as f:
            content = f.read().strip()
            if content:
                money = int(content)
            else:
                money = 0
    except (ValueError , FileNotFoundError):
        money = 0
    print(f'your account balance is {money}')
    return money

def wallet_add():
    money = wallet_read()
    while True:
        try:
            add_funds = int(input('how much more funds do you want to add?\n: '))
            if add_funds < 0:
                print('you cannot add negative funds')
                continue
            break
        except ValueError:
            print('please enter a number')
    new_money = money + add_funds
    with open ('wallet.txt' , 'w') as f:
        f.write(str(new_money))
    print(f'your new account balance is {new_money}')

def wallet_payout():
    money = wallet_read()
    while True:
        try:
            payout = int(input('how much do you want to payout?\n: '))
            if payout < 0:
                print('you cannot payout negative money')
                continue
            elif payout > money:
                print('your payout is higher then your account balance')
                continue
            break
        except ValueError:
            print('please enter a number')
    new_money = money - payout
    with open ('wallet.txt' , 'w') as f:
        f.write(str(new_money))
    print(f'your new account balance is {new_money}')

def game_round():
    deck = deck_refresh()
    dealer_cards , dealer_hand = dealer_turn(deck)
    time.sleep(1)
    player_cards , player_hand = player_turn(deck)
    player_cards = check_ace_player(player_hand , player_cards)
    time.sleep(1)
    dealer_cards = check_ace_dealer(dealer_hand , dealer_cards)
    while int(player_cards) < 21:
        answer1 = str(input('hit or stay : '))
        if answer1.lower() == 'hit':
            new_card = hit(deck)
            player_cards += new_card
            player_hand.append(new_card)
            print(f'your new cards value = {player_cards}')
            time.sleep(1)
            player_cards = check_ace_player(player_hand , player_cards)
        elif answer1.lower() == 'stay':
            print(f'your final cards value = {player_cards}')
            time.sleep(1)
            break
    while int(dealer_cards) < 17:
        print('dealers next card')
        time.sleep(1)
        new_card = hit(deck)
        dealer_cards += new_card
        dealer_hand.append(new_card)
        print(f'dealers new cards value = {dealer_cards}')
        time.sleep(1)
        dealer_cards = check_ace_dealer(dealer_hand , dealer_cards)
    outcome = check_game(player_cards , dealer_cards)
    if outcome == 'w':
        return 'w'
    elif outcome == 'l':
        return 'l'
    elif outcome == 'd':
        return 'd'

def game_main():
    while True:
        balance = wallet_read()
        bet = bet_amount(balance)
        result = game_round()
        change = calculate_money(bet , result)
        new_balance = balance + change
        with open("wallet.txt", 'w') as f:
            f.write(str(new_balance))
        print(f'your new balance is {new_balance} ')
        choice = play_again()
        if choice == 'y':
            continue
        if choice == 'n':
            break

menu_black()