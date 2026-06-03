import secrets

def main(game):
    if game == "lotto":
        identifier = "Lotto"
    if game == "vik":
        identifier = "Vikinglotto"
    if game == "ejp":
        identifier = "Eurojackpot"

    rows_played, money_spent, time_elapsed = 0, 0, 0

    def create_row():
        num_regular, num_star, row = [], [], []

        nums_1_5 = [1, 2, 3, 4, 5]

        nums_1_12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        nums_1_40 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

        nums_1_48 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48]

        nums_1_50 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

        def choose_numbers(max, list, type):
            for i in range(0, max):
                num = secrets.choice(list);  list.remove(num);  type.append(num)
            
            type.sort();  row.append(type)

        if game == "lotto":
            choose_numbers(7, nums_1_40, num_regular);  choose_numbers(0, nums_1_5, num_star)
        if game == "vik":
            choose_numbers(6, nums_1_48, num_regular);  choose_numbers(1, nums_1_5, num_star)
        if game == "ejp":
            choose_numbers(5, nums_1_50, num_regular);  choose_numbers(2, nums_1_12, num_star)

        return row
    
    print(f"\nRunning...\n")
    
    while True:
        machine, player = create_row(), create_row();  rows_played += 1
        
        if game == "lotto" or game == "vik":
            money_spent += 1;  time_elapsed += 7
        if game == "ejp":
            money_spent += 2;  time_elapsed += 3

        regular = len(set(machine[0]) & set(player[0]));  star = len(set(machine[1]) & set(player[1]));  result = f"{regular} + {star}"
        
        if result == "7 + 0" or result == "6 + 1" or result == "5 + 2":
            print(f"\n\nJackpot! (€1-120M, {identifier})\n\nRows played: {rows_played:,.0f}   Money spent: {money_spent:,.0f}€   Time elapsed: {time_elapsed:,.0f} days ({time_elapsed / 365:,.2f} years)\n\nWinning row: {player}\n\n")

            break
        else:
            pass
        
main("ejp")