def run(_):
    step = 3
    buf = [0]
    cur = 0

    for i in range(1, 2018):
        cur = ((cur + step) % len(buf)) + 1
        buf.insert(cur, i)

    print(buf[cur + 1])
