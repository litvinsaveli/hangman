# Write your code here
import random

print("H A N G M A N")
# print("The game will be available soon.")

list_of_words = ["python", "java", "kotlin", "javascript"]
list_of_tries = []
word = random.choice(list_of_words)

length_word = len(word)
silence_word = length_word * "-"

unknown_word = list(silence_word)


def game_process():
    count = 0
    word_in_process = ""

    while count < 9:
        print()
        print("".join(unknown_word))
        # print("Input a letter: ")
        x = input("Input a letter: ")

        if x in list_of_tries:
            print("You've already guessed this letter")
            continue

        if len(x) != 1:
            print("You should input a single letter")

        elif x.isnumeric() or x.isupper() or x == "" or x.isalpha() is False:
            print("Please enter a lowercase English letter")

        elif word.find(x) != -1:

            if word.find(x) == word.rfind(x):
                unknown_word[word.find(x)] = x
                word_in_process = "".join(unknown_word)
                list_of_tries.append(x)

            elif word.find(x) != word.rfind(x):
                unknown_word[word.find(x)] = x
                unknown_word[word.rfind(x)] = x

                word_in_process = "".join(unknown_word)
                list_of_tries.append(x)

            if word_in_process == word:
                print()
                print(word_in_process)
                print("You guessed the word!")
                print("You survived!")
                break

        else:
            print("That letter doesn't appear in the word")
            list_of_tries.append(x)
            count += 1

        if count == 8:
            print("You lost!")
            break


def game_start():
    gameplay = 0
    while gameplay < 1:
        print("Type 'play' to play the game, 'exit' to quit:")
        game = input()

        if game == "play":
            gameplay += 1
            game_process()
        elif game == "exit":
            break
        else:
            game_start()


game_start()
