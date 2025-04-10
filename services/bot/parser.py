import re

def normalize_stats(raw_text):
    lines = raw_text.splitlines()
    header_keywords = ["PTS", "AST", "REB", "STL", "BLK", "TO", "PF"]

    stat_lines = []
    for line in lines:
        line = line.strip()
        if len(line.split()) >= 8:
            stat_lines.append(line)

    players = []
    for line in stat_lines:
        parts = re.split(r"\s{2,}|\t|\s(?=\d)\s?", line)
        if len(parts) < 8:
            continue
        name = parts[0].strip()
        stats = list(map(int, re.findall(r"\d+", ' '.join(parts[1:]))))
        if len(stats) >= 7:
            players.append({
                "name": name,
                "team": "Unknown",
                "PTS": stats[0], "AST": stats[1], "REB": stats[2],
                "STL": stats[3], "BLK": stats[4], "TO": stats[5], "PF": stats[6]
            })

    return players if players else []
