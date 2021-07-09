import tmdb_client
from unittest.mock import Mock



def test_get_single_movie(monkeypatch):
    mock_single_movie = {'title': "Cruella"}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)

    single_movie = tmdb_client.get_single_movie(22)
    assert single_movie == mock_single_movie



def test_get_poster_url(monkeypatch):
    mock_poster_path = 'some-poster-path'
    request_mock = Mock()
    response = request_mock.return_value
    response.return_value = mock_poster_path
    expected_default_size = 'w342'
    monkeypatch.setattr('tmdb_client.requests.get', request_mock)

    poster_url = tmdb_client.get_poster_url(api_image_path=mock_poster_path)
    assert expected_default_size in poster_url


def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = {'cast': ['aaa', 'bbb']}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)

    single_movie_cast = tmdb_client.get_single_movie_cast(3)
    assert single_movie_cast is not None