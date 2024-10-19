# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44  # Размер дискеты в Мб
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50    # Число строк на странице
chars_per_line = 25    # Количество символов в строке
bytes_per_char = 4     # Количество байт для хранения одного символа

disk_size_bytes = disk_size_mb * 1024 * 1024

# Найдем объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Посчитаем количество книг, помещающихся на дискету
number_of_books = disk_size_bytes // book_size_bytes



print("Количество книг, помещающихся на дискету:",int(number_of_books))
