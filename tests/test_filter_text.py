import pytest
import os
from main import filter_text

@pytest.fixture
def temp_file(tmp_path):
    """
        Fixture to create a temporary text file with sample content for testing.

        Returns:
            str: Path to the temporary file.
    """
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
    """
        Test the filter_text function with a fixture.

        Parameters:
            temp_file (str): Path to the temporary file.

        Returns:
            None
    """
    keyword = 'перевірка'
    output_path = temp_file.parent/'filtered.txt'

    filter_text(temp_file, output_path, keyword)

    with open(output_path, 'r', encoding='utf-8') as filtered_file:
        filtered_content = filtered_file.read()

    assert keyword in filtered_content

    os.remove(output_path)


@pytest.mark.parametrize("input_text, exp_text, keyword",[
    ("Це тест\nЙде перевірка\nВсе", "Йде перевірка", "перевірка"),
    ("Тут нічого нема\nВсе ще нема", "", "перевірка"),
    ("перевірка\nперевірка перевірка", "перевірка\nперевірка перевірка", "перевірка"),
])
def test_filter_text_param(input_text, exp_text, keyword, tmp_path):
    """
        Test the filter_text function with parameterization.

        Parameters:
            input_text (str): Input text for testing.
            exp_text (str): Expected filtered text.
            keyword (str): Keyword for filtering.

        Returns:
            None
    """
    input_path = tmp_path / 'test_file.txt'
    output_path = tmp_path / 'output.txt'

    with open(input_path, 'w', encoding='utf-8') as file:
        file.write(input_text)

    filter_text(input_path, output_path, keyword)

    with open(output_path, 'r', encoding='utf-8') as file:
        result = file.read().strip()

    assert result == exp_text.strip()

    os.remove(input_path)
    os.remove(output_path)



