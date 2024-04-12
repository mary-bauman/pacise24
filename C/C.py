from sys import stdin

m = "abcdefghijklmnopqrstuvwxyz"

def get_word_number(word):
    return sum([(m.index(c) + 1) * (26 ** i) for i, c in enumerate(reversed(word))])

def get_word(number):
    o = []
    while number != 0:
        rem = number % 26
        o.append(m[rem - 1])
        number //= 26
    o.reverse()
    return "".join(o)

def main():
    for line in stdin:
        try:
            num = int(line[:-1])
            word = get_word(num)
            print(f"{word} {num}")
        except ValueError:
            word = line[:-1]
            num = get_word_number(word)
            print(f"{word} {num}")

main()
