from math import inf

def run(_):
    # Player, Boss, is player turn, poison turns, shield turns, recharge turns, mana spent
    s = [(True, 50, 500, 55, 0, 0, 0, 0)]
    lw = inf
    while len(s) > 0:
        p_turn, p_hp, p_mana, b_hp, p_t, s_t, r_t, spent = s.pop()

        if spent >= lw:
            continue

        if p_turn:
            p_hp -= 1
            if p_hp <= 0:
                continue

        if p_t > 0:
            p_t -= 1
            b_hp -= 3
        if s_t > 0:
            s_t -= 1
        if r_t > 0:
            r_t -= 1
            p_mana += 101
        
        if b_hp <= 0:
            if spent < lw:
                lw = spent
            continue
        
        if p_turn:
            if p_mana >= 53:
                s.append((False, p_hp, p_mana - 53 , b_hp - 4, p_t, s_t, r_t, spent + 53))
            if p_mana >= 73:
                s.append((False, p_hp + 2, p_mana - 73, b_hp - 2, p_t, s_t, r_t, spent + 73))
            if p_mana >= 113 and s_t == 0:
                s.append((False, p_hp, p_mana - 113, b_hp, p_t, 6, r_t, spent + 113))
            if p_mana >= 173 and p_t == 0:
                s.append((False, p_hp, p_mana - 173, b_hp, 6, s_t, r_t, spent + 173))
            if p_mana >= 229 and r_t == 0:
                s.append((False, p_hp, p_mana - 229, b_hp, p_t, s_t, 5, spent + 229))
        else:
            p_hp -= 1 if s_t > 0 else 8
            if p_hp <= 0: continue # Lose if player health drops below 0
            s.append((True, p_hp, p_mana, b_hp, p_t, s_t, r_t, spent))

    print(lw)
