import hashlib

def run(source):
    data = open(source).readline().strip()
    total = 1
    while True:
        hash = hashlib.md5(f"{data}{total}".encode()).hexdigest()
        if hash[0:5] == "00000":
            break

    print(total)
