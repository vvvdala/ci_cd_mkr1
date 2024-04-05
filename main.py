

def filter_text(input_path, output_path, keyword):
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        for line in input_file:
            if keyword in line:
                output_file.write(line)




