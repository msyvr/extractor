import langextract as lx
import logging
import os

# LangExtract parameters
model = "gpt-5-nano"
api_key = os.getenv("OPENAI_API_KEY")
max_workers = 6
passes = 1

def extract_data_from_text(documents:str, prompt:str, examples:list[any]):
    """Text analysis and data extraction based on provided examples."""

    result = lx.extract(
        text_or_documents=documents,
        prompt_description=prompt,
        examples=examples,
        model_id=model,
        api_key=api_key,        
        fence_output=True,
        extraction_passes=passes,
        max_workers=max_workers,
        debug=False
    )

    logging.info(f'Extraction result: {result.extractions}')

    return result