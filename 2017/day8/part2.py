import math
import re


def run(source):
    registers = {}
    instructions = open(source).readlines()
    re_str = "(\\w+) (dec|inc) (-?\\d+) if (\\w+) (==|!=|<|>|<=|>=) (-?\\d+)"
    highest = -math.inf

    for i in instructions:
        match = re.search(re_str, i)
        if not match:
            continue

        reg, op, amount, c_reg, c_op, c_amount = match.groups()
        c_amount = int(c_amount)
        reg_value = registers.get(c_reg, 0)

        if c_op == "==":
            condition = reg_value == c_amount
        elif c_op == "!=":
            condition = reg_value != c_amount
        elif c_op == "<":
            condition = reg_value < c_amount
        elif c_op == ">":
            condition = reg_value > c_amount
        elif c_op == "<=":
            condition = reg_value <= c_amount
        else:
            condition = reg_value >= c_amount

        if not condition:
            continue

        amount = int(amount) if op == "inc" else -int(amount)
        new_value = registers.get(reg, 0) + amount
        if new_value > highest:
            highest = new_value

        registers[reg] = new_value

    print(highest)
