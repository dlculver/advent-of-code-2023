
def get_winings(card: str) -> int:
    card = card.split(":")[-1].strip()
    winning_nums, your_nums = card.split("|")

    winning_nums = {int(num) for num in winning_nums.split()}

    your_nums = [int(num) for num in your_nums.split()]

    first_point = True
    
    winnings = 0

    for num in your_nums:
        if num in winning_nums and first_point:
            winnings += 1
            first_point = False
        elif num in winning_nums:
            winnings *= 2

    
    print(winnings)
    return winnings

def main():
    
    with open("input.txt", "r") as file:
        cards = file.readlines()

    print(cards)

    total_winnings = 0
    for card in cards: 
        total_winnings += get_winings(card)
    
    print(total_winnings)

if __name__ == "__main__":
    main()

