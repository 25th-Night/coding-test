def solution(new_id):
    new_id = new_id.lower()
    new_id2 = ""
    for c in new_id:
        if c.isalnum() or c in ["_", "-", "."]:
            new_id2 += c
    while ".." in new_id2:
        new_id2 = new_id2.replace("..", ".")
    if new_id2 and new_id2[0] == ".":
        new_id2 = new_id2[1:]
    if new_id2 and new_id2[-1] == ".":
        new_id2 = new_id2[:-1]
    if not new_id2:
        new_id2 = "a"
    if len(new_id2) >= 16:
        new_id2 = new_id2[:15]
    if new_id2[-1] == ".":
        new_id2 = new_id2[:-1]
    while len(new_id2) <= 2:
        new_id2 += new_id2[-1]
    return new_id2
        