# AI Research Intelligence Agent

A Python and FastAPI research tool that retrieves web search results and creates structured Markdown research briefs with source links.

## Features

- Web search through DuckDuckGo.
- Source titles, URLs and search snippets.
- Structured Markdown research briefs.
- FastAPI interactive documentation.
- Input validation and automated API tests.

## Requirements
Python 3.11 or newer.

## Setup - Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## API

`POST /research`

Example request:

```json
{
  "topic": "AI agents in scientific research",
  "max_sources": 5
}
```

## Tests

```cmd
pytest -q
```

## Limitations
Search snippets are not independently verified. This version does not use an LLM to synthesise or fact-check claims. Search availability depends on the external provider and network.

## Roadmap
- [ ] LLM-based evidence synthesis
- [ ] Citation verification
- [ ] Search-quality evaluation
- [ ] Docker deployment

## Author
Mohammed Asim - https://github.com/Whoisasimm
