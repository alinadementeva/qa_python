# qa_python
Список реализованных тестов:
1) test_add_new_book_add_two_books - тест на успешное добавление 2х книг в словарь
2) test_set_book_genre_set_genre_for_book - тест на проверку добавления жанра для книги, 
у которой до этого отсутствовал жанр в словаре
3) test_get_book_genre_book_has_no_genre - тест на проверку отсутствия жанра у книги в словаре
4) test_get_book_genre_get_books_by_genre - тест на получение жанра по книге,
у которой присутствует жанр в словаре
5) test_get_books_with_specific_genre_get_books_by_horror_genre - тест на успешное получение
списка книг по существующему жанру в словаре
6) test_get_books_with_specific_genre_genre_is_undefined - тест на проверку отсутствия
списка книг по несуществующему жанру
7) test_get_books_genre_books_genre_is_not_empty - тест на проверку, что словарь непустой 
8) test_get_books_for_children_get_children_books_list - тест на проверку, что в полученном
списке книг, подходящего для детей, отсутствуют книги в жанрах "Ужасы" и "Детективы"
9) test_add_book_in_favorites_invalid_books_names - тест на проверку, что невалидные значения
книг не попадают в список "Избранное" (3 невалидных значения: несуществующая книга в словаре,
пустое значение, пробел)
10) test_delete_book_from_favorites_delete_favorite_book - тест на проверку, что книга из списка
"Избранные" успешно удалена
11) test_get_list_of_favorites_books_get_favorite_books_list - тест на успешное получение
всех книг из списка "Избранное"