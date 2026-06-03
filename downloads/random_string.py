import secrets, math;  letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";  num = "0123456789"

symbols = "!@#$%^&*-_=+;:,.?";  symbols_extra = "()[]{}<>|~`";  symbols_all = symbols + symbols_extra

all_characters = letters + num + symbols_all

def main(generate, complexity, length):
    def test(string):
        # Approximate strength test based on combinatorics

        combinations = len(characters) ** len(string);  guess_time_years = (combinations / 10 ** 14) / 31557600

        # Entropy test

        entropy_bits = len(string) * math.log2(len(characters))


        if guess_time_years < 50:
            strength = "Guess time < 50 years, weak"
        if guess_time_years >= 50 and guess_time_years < 100:
            strength = f"Guess time ≈ {guess_time_years:,.1f} years, moderate"
        if guess_time_years >= 100:
            strength = f"Guess time ≈ {guess_time_years:,.1f} years, strong"

        if generate == 1:
            print(f"\n\n{string}\n\n\nDigits = {len(string)}\n\n{strength}\n\nEntropy ≈ {entropy_bits:,.0f} bits (< 40 = weak, 40 - 60 = moderate, 60 - 80 = strong, > 80 = very strong)\n\n")
        if generate == 0:
            print(f"\n\nDigits = {len(string)}\n\n{strength}\n\nEntropy ≈ {entropy_bits:,.0f} bits (< 40 = weak, 40 - 60 = moderate, 60 - 80 = strong, > 80 = very strong)\n\n")

    def generate_string():
        string = ""

        for i in range(0, length):
            string += secrets.choice(characters)

        test(string)

    def generation():
        global characters

        if complexity == 1:
            characters = letters;  generate_string()

        if complexity == 2:
            characters = letters + num;  generate_string()

        if complexity == 3:
            characters = letters + num + symbols;  generate_string()

        if complexity == 4:
            characters = all_characters;  generate_string()

    def user_input():
        global characters;  global length

        includes_letter = "0";  includes_num = "0";  includes_symbol = "0";  includes_exception = "0";  exceptions = ""

        string = input(f"\n\nType string here:\n\n").strip();  length = len(string)

        for i in string:
            if i in letters:
                includes_letter = "1"
            if i in num:
                includes_num = "1"
            if i in symbols_all:
                includes_symbol = "1"
            if i not in all_characters:
                includes_exception = "1"

                if i not in exceptions:
                    exceptions += i
                else:
                    pass

        variation = includes_letter + includes_num + includes_symbol

        if includes_exception == "1":
            print(f"\n\nString contains unlisted character(s): {exceptions}. Try again.");  user_input()

        if variation == "000":
            print(f"String may be empty. Try again.");  user_input()

        if variation == "100":
            characters = letters;  test(string)

        if variation == "010":
            characters = num;  test(string)

        if variation == "001":
            characters = symbols_all;  test(string)

        if variation == "110":
            characters = letters + num;  test(string)

        if variation == "011":
            characters = num + symbols_all;  test(string)

        if variation == "101":
            characters = letters + symbols_all;  test(string)

        if variation == "111":
            characters = letters + num + symbols_all;  test(string)

    if generate == 1:
        generation()

    if generate == 0:
        user_input()

main(1, 3, 14)