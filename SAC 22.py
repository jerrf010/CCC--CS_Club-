while True:
    w = str(input("Enter the wordle guess: ").lower())
    amount_of_vowels = 0
    if len(w) == 5:
        for i in range(len(w)):
            if w[i] == "a" or w[i] == "e" or w[i] == "i" or w[i] == "o" or w[i] == "u":
                amount_of_vowels += 1

        if amount_of_vowels >= 2:
            print("Good")
        else:
            print("Bad")

    else:
        print("Error: Word must be 5 letters")