import hashlib

def run(_):
    i = 1
    while True:
        if hashlib.md5(f"ckczppom{i}".encode()).hexdigest()[0:6] == "000000":
            break
        i += 1
    print(i)
