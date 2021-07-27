import Counter


def I_have_no_clue(word, letter):
    Counter = 0
    for temp in word:
        if temp == letter:
            Counter =+ 1
            return True
    return False

me = I_have_no_clue("straw", "o")

print(me)