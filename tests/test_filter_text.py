import pytest
import os
from main import filter_text

@pytest.fixture
def temp_file(tmp_path):
    text = """Текст для перевірки.
    Один. Два. Три.
    Перевіряємо ключове слово "перевірка"
    перевірка йде
    перевірка завершена"""

    file_path = tmp_path/ 'test_file.txt'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    return file_path

def test_filter_text_fix():



