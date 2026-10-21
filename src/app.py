from src.markov_chain import MarkovChain
from src.generator import generate
import sys

#creates user interface
while True:

    print()
    print("WELCOME TO A MUSIC GENERATOR!")
    print()
    print("Press Ctrl+C to stop running.")
    print()

    pic = ["⠀⠀⠀⠀⠀⠀⣼⣿⣿⣦⠀⠀⠀", "⠀⠀⠀⠀⠀⢰⣿⠁⠀⢹⡄⠀⠀", "⠀⠀⠀⠀⠀⢸⣿⠀⠀⣾⡇⠀⠀", "⠀⠀⠀⠀⠀⠈⣿⢀⣾⣿⠀⠀⠀", "⠀⠀⠀⠀⠀⣀⣿⣿⣿⠃⠀⠀⠀", "⠀⠀⠀⣠⣾⣿⣿⡟⠁⠀⠀⠀⠀", "⠀⢠⣾⣿⠟⠁⠘⡇⠀⠀⠀⠀⠀", "⢀⣿⡟⠁⠀⣠⣶⣿⣶⣶⣤⡀⠀", "⢸⣿⠀⠀⣼⣿⠟⢻⡛⠻⣿⣷⠀", "⠘⣿⡀⠀⢹⣇⠀⠘⡇⠀⠘⣿⠇", "⠀⠙⣷⡄⠀⠙⠂⠀⣷⠀⣸⡟⠀", "⠀⠀⠈⠙⠷⢦⣤⣤⣼⡞⠋⠀⠀", "⠀⠀⠀⠀⢀⣀⡀⠀⠸⡇⠀⠀⠀", "⠀⠀⠀⠀⣿⣿⣿⠀⢠⡇⠀⠀⠀", "⠀⠀⠀⠀⠈⠛⠷⠖⠋⠀⠀⠀⠀"]
    for line in pic:
        print(line)
    print()

    key = input("Choose key, write 'minors' or 'majors': ")
    if key not in ("minors", "majors"):
        print("!!! Please write a valid key.")
        continue
    print()
    degree = input("Choose degree (but note that the higher the degree, the shorter the generated song): ")
    try:
        degree = int(degree)
    except ValueError:
        print("!!! Please input an integer.")
        continue
    if degree <= 0:
        print("!!! Degree should be 1 or higher.")
        continue
    print()
    song_length = input("Choose what length you wish the song to be: ")
    try:
        song_length = int(song_length)
    except ValueError:
        print("!!! Please input an integer.")
        continue
    if song_length <= 0:
        print("!!! Song length should be 1 or higher.")
        continue
    print()
    file_name = input("Input what you want your generated song to be saved as: ")
    if len(file_name) == 0:
        print("!!! File name can not be empty.")
        continue
    if " " in file_name:
        print("!!! Please do not use spaces in the file name.")
        continue
    break

if key == "minors":
    m = MarkovChain("Minors", int(degree))
if key == "majors":
    m = MarkovChain("Majors", int(degree))

m.train()
generate(m.trie, song_length, file_name)

print("Your midi-file is ready, and you can find it from the generated_songs directory!")
print()
