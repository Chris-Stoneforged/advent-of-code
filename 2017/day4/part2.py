def run(source):
    print(sum(is_valid(line) for line in open(source).readlines()))


def is_valid(phrase: str) -> bool:
    words = [sorted_word(word) for word in phrase.split()]
    return not any(word for word in words if words.count(word) > 1)


def sorted_word(word: str):
    return sorted(ord(l) for l in word)
