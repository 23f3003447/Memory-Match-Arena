import pytest
from app import create_app
from game_rules import calculate_score, validate_result


@pytest.fixture()
def client(tmp_path):
    app = create_app({'TESTING': True, 'DATABASE': str(tmp_path / 'test.db')})
    return app.test_client()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Memory Match Arena' in response.data


def test_empty_leaderboard(client):
    response = client.get('/api/leaderboard?difficulty=easy')
    assert response.status_code == 200
    assert response.json == {'results': []}


def test_valid_score_and_leaderboard(client):
    response = client.post('/api/scores', json={'player': 'Mahesh', 'difficulty': 'easy', 'seconds': 40, 'moves': 8})
    assert response.status_code == 201
    assert response.json['score'] == calculate_score('easy', 40, 8)
    board = client.get('/api/leaderboard?difficulty=easy').json['results']
    assert len(board) == 1
    assert board[0]['player'] == 'Mahesh'


@pytest.mark.parametrize('payload', [
    {'player': '<script>', 'difficulty': 'easy', 'seconds': 20, 'moves': 6},
    {'player': 'OK', 'difficulty': 'unknown', 'seconds': 20, 'moves': 6},
    {'player': 'OK', 'difficulty': 'easy', 'seconds': -1, 'moves': 6},
    {'player': 'OK', 'difficulty': 'easy', 'seconds': 20, 'moves': 2},
    {'player': 'OK', 'difficulty': 'easy', 'seconds': True, 'moves': 6},
])
def test_invalid_scores_rejected(client, payload):
    assert client.post('/api/scores', json=payload).status_code == 400


def test_invalid_payload_rejected(client):
    assert client.post('/api/scores', data='not-json').status_code == 400
    assert client.get('/api/leaderboard?difficulty=unknown').status_code == 400


def test_score_formula_and_basic_validation():
    assert calculate_score('easy', 1, 6) == 1497
    assert validate_result('medium', 10, 8) is None
    assert validate_result('hard', 10, 6) is not None
