from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="AI Research Intelligence Agent",
    description="An API for structured research planning.",
    version="0.1.0",
)


class ResearchRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=500)
    research_questions: list[str] = Field(default_factory=list, max_length=10)


@app.get("/")
def root():
    return {
        "name": "AI Research Intelligence Agent",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/research/plan")
def create_research_plan(request: ResearchRequest):
    questions = request.research_questions or [
        f"What is the current state of {request.topic}?",
        f"What are the main challenges in {request.topic}?",
        f"What evidence supports current findings about {request.topic}?",
    ]

    return {
        "topic": request.topic,
        "research_questions": questions,
        "status": "plan_created",
        "note": "Research planning only; web search is not implemented yet.",
    }