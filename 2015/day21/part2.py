from itertools import combinations

def run(source):
    player = (100, 0, 0)
    boss = (100, 8, 2)
    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]
    armor = [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]
    rings = [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3)
    ]
    def does_player_win(item_combo):
        _, p_dmg, p_arm = item_combo
        return boss[0] / max(1, p_dmg - boss[2]) <= player[0] / max(1, boss[1] - p_arm)

    items = []
    for w in combinations(weapons, 1):
        for a in combinations(armor, 1):
            for r in combinations(rings, 2):
                items.append(tuple(sum(elements) for elements in zip(w[0], a[0], r[0], r[1])))

    items = sorted([i for i in items if not does_player_win(i)], key=lambda x: x[0], reverse=True)
    print(items[0][0])
