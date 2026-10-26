# AI Research Intelligence Agent

A Python and FastAPI project for structured research planning, designed to evolve into an evidence-grounded AI research assistant.

## Current Features

- FastAPI application and interactive API documentation.
- Health-check endpoint.
- Research-plan generation from a topic and optional questions.
- Input validation with Pydantic.

## Requirements

Python 3.11 or newer.

## Setup

```bash
python -m venv .venv
```

On Windows:

```cmd
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs to explore the API.

## Example Request

```json
{
  "topic": "AI agents in scientific research",
  "research_questions": [
    "What are the main applications?",
    "What are the limitations?"
  ]
}
```

Send the example to POST /research/plan using the interactive API documentation.

## Roadmap

- [ ] Web search integration.
- [ ] Source extraction and reference tracking.
- [ ] LLM-powered evidence synthesis.
- [ ] Automated tests and research-quality evaluation.
- [ ] Docker support.

## Current Limitations

This initial version generates research plans only. It does not yet search the web, verify citations, or generate evidence-based research reports.

## License

No license has been specified yet. Add a LICENSE file before defining reuse permissions.
