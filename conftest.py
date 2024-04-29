import pytest

from main import BooksCollector

@pytest.fixture
def books_genre():
    books_genre = BooksCollector()
    books_genre.books_genre = {
        'Война миров': '',
        'Восточный экспресс': 'Детектив',
        'Дракула': 'Ужасы',
        'Плоский мир': '',
        'Франкенштейн': 'Ужасы',
        'Всё о Муми-троллях': 'Мультфильмы',
        'На выручку юному Гасси!': 'Комедии',
        'Хроники Нарнии': 'Фантастика'
    }
    return books_genre
