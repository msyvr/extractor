import langextract as lx
    
def save_result(result:any, text_description:str, output_dir:str, output_filename:str):
    output_file = '.'.join([output_filename, "jsonl"])
    lx.io.save_annotated_documents([result], output_dir=output_dir, output_name=output_file)
    print(f'Results for {text_description} saved to {output_dir}/{output_file}')

    viz_filename = output_filename + "_viz"
    viz_file = '.'.join([viz_filename,"html"])
    viz_path = f'{output_dir}/{viz_file}'

    html_content = lx.visualization.visualize(f'{output_dir}/{output_file}')
    with open(viz_path, 'w') as f:
        f.write(str(html_content))
    print(f'Vizualization saved to: {output_dir}/{viz_file}')

def view_tokenization(result):
    for entity in result.extractions:
        position = ""
        if entity.char_interval:
            start = entity.char_interval.start_pos
            end = entity.char_interval.end_pos
            position = f" (chars {start}-{end})"
        
        print(f'* {entity.extraction_class.upper()}: {entity.extraction_text}{position}')

