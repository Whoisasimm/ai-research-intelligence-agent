from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="AI Research Intelligence Agent",
    description=(
        "A research API for organising research questions, "
        "tracking sources, and producing structured research briefs."
    ),
    version="0.1.0",
)


class ResearchRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=500)
    research_questions: list[str] = Field(default_factory=list, max_length=10)


class ResearchBrief(BaseModel):
    topic: str
    research_questions: list[str]
    status: str
    note: str


@app.get("/")
def root():
    return {
        "name": "AI Research Intelligence Agent",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/research/plan", response_model=ResearchBrief)
def create_research_plan(request: ResearchRequest):
    questions = request.research_questions or [
        f"What is the current state of {request.topic}?",
        f"What are the main challenges and limitations of {request.topic}?",
        f"What evidence supports the main findings about {request.topic}?",
    ]

    return ResearchBrief(
        topic=request.topic,
        research_questions=questions,
        status="plan_created",
        note=(
            "Research plan created. Web retrieval and evidence-based "
            "synthesis are not yet implemented."
        ),
    )