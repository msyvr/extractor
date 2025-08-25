# Extractor

Extract structured data from unstructured text.

For the literature example, inputs (unstructured text):

![shakespeare quotes](/assets/images/shakespeare_quotes.png)

and output (json):

![structured output](/assets/images/structured_output.png)

LangExtract has a built-in visualizer. Scrolling through the document, extracted data is displayed and the associated text highlighted.

![shakespeare mp4](/assets/images/shakespeare.mp4)

## Use

```bash
git clone git@github.com/msyvr/chattitor
```

This project uses LLM calls via LangExtract. , add your own `.env` file. Make sure .gitignore includes `.env` and then add your OPENAI_API_KEY to `.env`.

In uv, there's no need to use python-dotenv if a `.env` file is present, but you do need to give `uv` permission to access it. To do that:

```bash
export UV_ENV_FILE=".env"
```

### Streamlit app example

For Streamlit to access api keys so llm calls can be made from the interactive app, put keys into `.streamlit/secrets.toml` and verify it's in `.gitignore`.

## FYI

### OpenAI API usage

[Dashboard](https://platform.openai.com/usage)
