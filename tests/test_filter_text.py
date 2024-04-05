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

def test_filter_text_fix(temp_file):
    keyword = 'перевірка'
    output_path = temp_file.parent/'filtered.txt'

    filter_text(temp_file, output_path, keyword)

    with open(output_path, 'r', encoding='utf-8') as filtered_file:
        filtered_content = filtered_file.read()

    assert keyword in filtered_content

    os.remove(output_path)






