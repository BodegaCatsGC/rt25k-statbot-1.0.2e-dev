from services.bot.parser import normalize_stats

def test_normalize_stats():
    raw_text = "Player1 10 5 7 2 1 3 2\nPlayer2 20 8 10 3 2 4 3"
    result = normalize_stats(raw_text)
    assert len(result) == 2
    assert result[0]["name"] == "Player1"
    assert result[1]["PTS"] == 20