import re

def run(source):
    def is_nice(x):
        return re.search("([a-z])[a-z]\\1", x) and re.search("([a-z][a-z]).*\\1", x)
    print(len([line for line in open(source) if is_nice(line.strip())]))
