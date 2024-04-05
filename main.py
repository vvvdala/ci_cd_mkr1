def filter_text(input_path: str, output_path: str, keyword: str):
    """

        Parameters:
        input_path (str): The path to the input text file to be processed.
        output_path (str): The path to the file where the filtered text will be saved.
        keyword (str): The keyword for filtering.

        Returns:
        None
        """
    with open(input_path, 'r', encoding='utf-8') as input_file, open(output_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            if keyword in line:
                output_file.write(line)

input_path = 'my_text_file.txt'
output_path = 'filtered.txt'

keyword = 'перевірка'

filter_text(input_path, output_path, keyword)

print("Результат збережено у файлі 'filtered.txt'.")



