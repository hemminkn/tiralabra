from markov_chain import MarkovChain
from generator import generate
import sys

while True:

    print()
    print("WELCOME TO A MUSIC GENERATOR!")
    print()

    pic = ["⠀⠀⠀⠀⠀⠀⣼⣿⣿⣦⠀⠀⠀", "⠀⠀⠀⠀⠀⢰⣿⠁⠀⢹⡄⠀⠀", "⠀⠀⠀⠀⠀⢸⣿⠀⠀⣾⡇⠀⠀", "⠀⠀⠀⠀⠀⠈⣿⢀⣾⣿⠀⠀⠀", "⠀⠀⠀⠀⠀⣀⣿⣿⣿⠃⠀⠀⠀", "⠀⠀⠀⣠⣾⣿⣿⡟⠁⠀⠀⠀⠀", "⠀⢠⣾⣿⠟⠁⠘⡇⠀⠀⠀⠀⠀", "⢀⣿⡟⠁⠀⣠⣶⣿⣶⣶⣤⡀⠀", "⢸⣿⠀⠀⣼⣿⠟⢻⡛⠻⣿⣷⠀", "⠘⣿⡀⠀⢹⣇⠀⠘⡇⠀⠘⣿⠇", "⠀⠙⣷⡄⠀⠙⠂⠀⣷⠀⣸⡟⠀", "⠀⠀⠈⠙⠷⢦⣤⣤⣼⡞⠋⠀⠀", "⠀⠀⠀⠀⢀⣀⡀⠀⠸⡇⠀⠀⠀", "⠀⠀⠀⠀⣿⣿⣿⠀⢠⡇⠀⠀⠀", "⠀⠀⠀⠀⠈⠛⠷⠖⠋⠀⠀⠀⠀"]
    for line in pic:
        print(line)
    print()

    key = input("Choose key, write 'minors' or 'majors': ")
    if key not in ("minors", "majors"):
        print("Please write a valid key.")
        continue
    print()
    degree = input("Choose degree: ")
    try:
        degree = int(degree)
    except ValueError:
        print("Please input an integer.")
        continue
    if degree <= 0:
        print("Degree should be 1 or higher")
        continue
    break

if key == "minors":
    m = MarkovChain("Minors", int(degree))
if key == "majors":
    m = MarkovChain("Majors", int(degree))

m.train()
file = generate(m.trie)

print("Your midi-file is ready!")
print()
