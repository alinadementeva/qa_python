from main import BooksCollector

import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Энн из Зелёных крыш')
        collector.add_new_book('Автостопом по галактике')

        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_set_genre_for_book(self, books_genre):
        books_genre.set_book_genre('Плоский мир', 'Фантастика')
        book_genre = books_genre.get_book_genre('Плоский мир')

        assert book_genre == 'Фантастика'

    def test_get_book_genre_book_has_no_genre(self, books_genre):
        book_genre = books_genre.get_book_genre('Война миров')

        assert book_genre == ''

    def test_get_book_genre_get_books_by_genre(self, books_genre):
        book = books_genre.get_book_genre('На выручку юному Гасси!')

        assert book == 'Комедия'

    def test_get_books_with_specific_genre_get_books_by_horror_genre(self, books_genre):
        books_list = books_genre.get_books_with_specific_genre('Ужасы')

        assert books_list == ['Дракула', 'Франкенштейн']

    def test_get_books_with_specific_genre_genre_is_undefined(self, books_genre):
        books_list = books_genre.get_books_with_specific_genre('Приключения')

        assert books_list == []

    def test_get_books_genre_books_genre_is_not_empty(self, books_genre):

        assert len(books_genre.get_books_genre()) != 0

    def test_get_books_for_children_get_children_books_list(self, books_genre):
     books_for_children = []
     result = books_genre.get_books_for_children()
     books_for_children.append(result)

     assert books_for_children != ['Восточный экспресс', 'Дракула', 'Франкенштейн']

    @pytest.mark.parametrize('name',
                             [
                                 'Денискины рассказы',
                                 '',
                                 ' '
                             ])
    def test_add_book_in_favorites_invalid_books_names(self, name):
        collector = BooksCollector()

        favorite_books = collector.add_book_in_favorites(name)

        assert favorite_books == None

    def test_delete_book_from_favorites_delete_favorite_book(self, books_genre):
        books_genre.add_book_in_favorites('Франкенштейн')
        books_genre.add_book_in_favorites('Восточный экспресс')
        books_genre.delete_book_from_favorites('Франкенштейн')
        favorite_books_list = books_genre.get_list_of_favorites_books()

        assert favorite_books_list == ['Восточный экспресс']

    def test_get_list_of_favorites_books_get_favorite_books_list(self, books_genre):

        books_genre.add_book_in_favorites('На выручку юному Гасси!')
        books_genre.add_book_in_favorites('Плоский мир')
        books_genre.add_book_in_favorites('Всё о Муми-троллях')

        favorites_book_list = books_genre.get_list_of_favorites_books()

        assert favorites_book_list == ['На выручку юному Гасси!', 'Плоский мир', 'Всё о Муми-троллях']


