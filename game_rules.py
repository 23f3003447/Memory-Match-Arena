"""Difficulty configuration, score calculation, and basic input validation."""
DIFFICULTIES = {
    'easy': {'pairs': 6, 'columns': 4, 'label': 'Easy'},
    'medium': {'pairs': 8, 'columns': 4, 'label': 'Medium'},
    'hard': {'pairs': 12, 'columns': 6, 'label': 'Hard'},
}


def validate_result(difficulty, seconds, moves):
    if difficulty not in DIFFICULTIES:
        return 'Invalid difficulty.'
    if type(seconds) is not int or not 1 <= seconds <= 3600:
        return 'Time must be an integer between 1 and 3600 seconds.'
    if type(moves) is not int or not DIFFICULTIES[difficulty]['pairs'] <= moves <= 1000:
        return 'Invalid move count.'
    return None


def calculate_score(difficulty, seconds, moves):
    """Reward matching more pairs, with smaller time/move penalties."""
    pairs = DIFFICULTIES[difficulty]['pairs']
    return max(100, pairs * 250 - seconds * 3 - (moves - pairs) * 20)
