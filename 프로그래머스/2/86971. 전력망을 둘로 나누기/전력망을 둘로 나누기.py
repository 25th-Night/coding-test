from copy import deepcopy

def solution(n, wires):
    diff_list = []

    for wire in wires:
        new_wires = deepcopy(wires)
        new_wires.remove(wire)
        part_a = {wire[0]}
        part_b = set()
        while (part_a != part_b) :
            part_b = deepcopy(part_a)
            for wire in new_wires:
                if (part_a & set(wire)):
                    part_a |= set(wire)  
        diff_list.append(abs((n - 2 * len(part_a))))

    return min(diff_list)