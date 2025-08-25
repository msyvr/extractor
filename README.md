# Extractor

A CLI utility for extracting structured data from unstructured text. Uses [LangExtract](https://github.com/google/langextract), an open source Python library.

Examples are ready to run out of the box after downloading and adding your API key (see below for details). An example output for the Shakespearean text example:

| Input                                           | Output                                        |
| ----------------------------------------------- | --------------------------------------------- |
| ![quote](/assets/images/shakespeare_quotes.png) | ![json](/assets/images/structured_output.png) |

LangExtract has a built-in visualizer. Scrolling through the document, extracted data is displayed and the associated text highlighted.

https://github.com/user-attachments/assets/96aebae9-7423-4258-97a2-35ae4ce6e667

## Use

```bash
git clone git@github.com/msyvr/extractor
```

This project uses LangExtract together with an LLM, and [custom model providers can be added](https://github.com/google/langextract?tab=readme-ov-file#adding-custom-model-providers) via a lightweight plug-in system. The example uses an economical OpenAI model.

For api keys, add a `.env` file and ensure that it's included in .gitignore to avoid exposing keys.

Give `uv` permission to access `.env`:

```bash
export UV_ENV_FILE=".env"
```

Run the Shakespeare text example:

```bash
uv run main.py
```

## Why build this?

An initial experiment with Google's [LangExtract](https://github.com/google/langextract).

Not included here (yet) but, ultimately, build graph visualizations with extracted entities as nodes and extracted relationships as edges.

## LLM usage

This example uses `gpt-5-nano` which trades off significant quality for lower cost. It's worth experimenting to identify an LLM to balance quality/cost.

[Dashboard](https://platform.openai.com/usage)
