from typing import List
from collections import deque


def run(source):
    instructions: List[List[str]] = [
        l.rstrip().split(" ") for l in open(source).readlines()
    ]

    state = {
        "prog": 0,
        "b_sent": 0,
        0: {"cur": 0, "jmp": 0, "p": 0},
        1: {"cur": 0, "jmp": 0, "p": 1},
    }
    messages = {0: deque(), 1: deque()}

    def get_value(program: int, value: str) -> int:
        return (
            int(value)
            if value.lstrip("-").isnumeric()
            else state[program].get(value, 0)
        )

    def set_value(program: int, register: str, value: int):
        state[program][register] = value

    def send(program: int, register: str):
        messages[program].append(get_value(program, register))
        if program == 1:
            state["b_sent"] += 1

    def receive(program: int, register: str):
        q = messages[abs(program - 1)]
        if not len(q):
            state["prog"] = abs(program - 1)
            return 1

        set_value(program, register, q.popleft())

    def jump(program: int, register: str, value: str):
        if get_value(program, register) > 0:
            state[program]["jmp"] = get_value(program, value)

    ops = {
        "snd": lambda p, args: send(p, args[0]),
        "set": lambda p, args: set_value(p, args[0], get_value(p, args[1])),
        "add": lambda p, args: set_value(
            p, args[0], get_value(p, args[0]) + get_value(p, args[1])
        ),
        "mul": lambda p, args: set_value(
            p, args[0], get_value(p, args[0]) * get_value(p, args[1])
        ),
        "mod": lambda p, args: set_value(
            p, args[0], get_value(p, args[0]) % get_value(p, args[1])
        ),
        "rcv": lambda p, args: receive(p, args[0]),
        "jgz": lambda p, args: jump(p, args[0], args[1]),
    }

    deadlock_count = 0
    while True:
        if deadlock_count > 2:
            print(state["b_sent"])
            break

        program = state["prog"]
        state[program]["jmp"] = 1
        current = state[program]["cur"]

        if current < 0 or current >= len(instructions):
            deadlock_count += 1
            state["prog"] = abs(program - 1)
            continue

        instruction = instructions[current]
        if ops[instruction[0]](program, instruction[1:]) == 1:
            deadlock_count += 1
            continue

        state[program]["cur"] += state[program]["jmp"]
        deadlock_count = 0
