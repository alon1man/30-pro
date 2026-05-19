import os

F = "data\\name.txt"
G = "data\\diff.txt"
T = "data\\score.txt"

def savename(t):
    with open(F, "a", encoding="utf8") as file:
        file.write(t + "\n")

def savediff(t):
    with open(G, "a", encoding="utf8") as file:
        file.write(t + "\n")

def savescore(t):
    with open(T, "a", encoding="utf8") as file:
        file.write(t + "\n")

def showname(): 
    if os.path.exists(F):
        with open(F, "r", encoding="utf8") as file:
            content = file.read()
            print(content)
def _read_lines(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    return []
def showdiff(): 
    if os.path.exists(G):
        with open(G, "r", encoding="utf8") as file:
            content = file.read()
            print(content)

def showscore(): 
    if os.path.exists(T):
        with open(T, "r", encoding="utf8") as file:
            content = file.read()
            print(content)
            
def load_leaderboard():
    names = _read_lines(F)
    diffs = _read_lines(G)
    scores = _read_lines(T)
    entries = []
    max_len = max(len(names), len(diffs), len(scores))
    for i in range(max_len):
        entries.append({
            "name": names[i] if i < len(names) else "",
            "diff": diffs[i] if i < len(diffs) else "",
            "time": scores[i] if i < len(scores) else ""
        })
    return entries


def parse_time_to_seconds(timestr):
    try:
        parts = timestr.split(":")
        if len(parts) == 2:
            minutes = int(parts[0])
            seconds = int(parts[1])
            return minutes * 60 + seconds
    except Exception:
        pass
    return None


def load_leaderboard_sorted():
    entries = load_leaderboard()
    sorted_entries = sorted(
        entries,
        key=lambda e: parse_time_to_seconds(e["time"]) if parse_time_to_seconds(e["time"]) is not None else float("inf")
    )
    return sorted_entries
