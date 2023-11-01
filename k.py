import itertools

def generate_permutations(arr, length):
    permutations = list(itertools.product(arr, repeat=length))
    return permutations

letters = ['a', 'b', 'c']
user_input = int(input("Podaj liczbę: "))

if user_input <= len(letters):
    permutations = generate_permutations(letters, user_input)
    for p in permutations:
        print("".join(p))
else:
    print("Podano zbyt dużą liczbę. Maksymalna długość to", len(letters))
