import os
from examples.literature import shakespeare
import time
from src import view_result


def extract_data():
    example_type = input('Select example from literature (l): ')
    output_filename = input('(OPTIONAL): Enter the filename for the results: ')
    output_dir = "results"


    if example_type in {"literature", "l"}:
        type = "literature text extraction"
        print(f'LangExtract: {type}')
        start = time.perf_counter()
        doc_size, text_description = shakespeare(output_dir, output_filename)
        end = time.perf_counter()
        elapsed = end - start
        print(f'{text_description.capitalize()} processed by LangExtract.\nSize: {doc_size} bytes \nTime elapsed: {elapsed}')
    else:
        print(f'The example type selected is not available.')

if __name__ == "__main__":
    extract_data()
