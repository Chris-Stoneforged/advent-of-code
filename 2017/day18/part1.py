from typing import Dict, List


def run(source):
    instructions: List[List[str]] = [
        l.rstrip().split(" ") for l in open(source).readlines()
    ]
    registers: Dict[str, int] = {"cur": 0, "jmp": 0, "snd": 0, "rcv": 0}

    def get_value(value: str) -> int:
        return int(value) if value.lstrip("-").isnumeric() else registers.get(value, 0)

    def set_value(register: str, value: int):
        registers[register] = value

    def play_sound(register: str):
        registers["snd"] = registers.get(register, 0)

    def jump(register: str, value: str):
        if get_value(register) > 0:
            registers["jmp"] = get_value(value)

    def recover(register: str):
        if get_value(register) != 0:
            registers["rcv"] = registers["snd"]
            print(registers["rcv"])
            exit()

    ops = {
        "snd": lambda args: play_sound(args[0]),
        "set": lambda args: set_value(args[0], get_value(args[1])),
        "add": lambda args: set_value(args[0], get_value(args[0]) + get_value(args[1])),
        "mul": lambda args: set_value(args[0], get_value(args[0]) * get_value(args[1])),
        "mod": lambda args: set_value(args[0], get_value(args[0]) % get_value(args[1])),
        "rcv": lambda args: recover(args[0]),
        "jgz": lambda args: jump(args[0], args[1]),
    }

    try:
        while True:
            registers["jmp"] = 1
            instruction = instructions[registers["cur"]]
            ops[instruction[0]](instruction[1:])
            registers["cur"] += registers["jmp"]
    except:
        pass
