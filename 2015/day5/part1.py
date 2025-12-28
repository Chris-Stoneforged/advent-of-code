def run(source):
    def is_nice(x):
        has_double = False
        prev = x[0]
        vowel_count = 1 if prev in ['a', 'e', 'i', 'o', 'u'] else 0
        for curr in x[1:]:
            print(prev + curr)
            for b in ["ab", "cd", "pq", "xy"]:
                if prev + curr == b:
                    return False
            if curr == prev:
                has_double = True
            if curr in ['a', 'e', 'i', 'o', 'u']:
                vowel_count += 1
            prev = curr

        return has_double and vowel_count >= 3

    print(len([line for line in open(source) if is_nice(line.strip())]))
