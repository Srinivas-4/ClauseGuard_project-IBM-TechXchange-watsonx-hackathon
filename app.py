from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Clause Guard API",
    version="1.0.0",
    description="API that provides contract clause classification, risk analysis, and rewrite suggestions."
)

# Input model
class ClauseRequest(BaseModel):
    clause: str

# Output models
class ClassificationResponse(BaseModel):
    classification: str

class RiskResponse(BaseModel):
    risk_level: str
    explanation: str

class RewriteResponse(BaseModel):
    suggestion: str


@app.post("/classify", response_model=ClassificationResponse)
def classify_clause(req: ClauseRequest):
    # Dummy logic (replace with AI or rules later)
    clause_text = req.clause.lower()
    if "payment" in clause_text:
        result = "Payment Obligation"
    elif "termination" in clause_text:
        result = "Termination Clause"
    else:
        result = "General Clause"
    return {"classification": result}


@app.post("/risk", response_model=RiskResponse)
def analyze_risk(req: ClauseRequest):
    # Dummy logic (replace with AI later)
    clause_text = req.clause.lower()
    if "penalty" in clause_text or "indemnity" in clause_text:
        return {"risk_level": "High", "explanation": "Clause may impose heavy penalties or liabilities."}
    elif "termination" in clause_text:
        return {"risk_level": "Medium", "explanation": "Clause allows early exit but could harm stability."}
    else:
        return {"risk_level": "Low", "explanation": "Clause is standard and low risk."}


@app.post("/rewrite", response_model=RewriteResponse)
def rewrite_clause(req: ClauseRequest):
    # Dummy logic (replace with AI later)
    return {
        "suggestion": f"Suggested clearer wording for clause: '{req.clause}'"
    }
