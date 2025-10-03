from fastapi import APIRouter, HTTPException
from api.models.requests import PatternRunRequest
from api.models.responses import PatternRunResponse

router = APIRouter(prefix="/patterns", tags=["patterns"])

AVAILABLE_PATTERNS = [
    "reflection", "tool_using", "react", "planning", "pev",
    "tree_of_thoughts", "multi_agent", "meta_controller", "blackboard",
    "ensemble", "episodic_semantic_memory", "graph_memory",
    "self_improvement", "dry_run_harness", "simulator",
    "reflexive_metacognitive", "cellular_automata"
]

@router.get("")
def list_patterns():
    return {"patterns": AVAILABLE_PATTERNS}

@router.post("/{pattern_name}/run", response_model=PatternRunResponse)
def run_pattern(pattern_name: str, request: PatternRunRequest):
    if pattern_name not in AVAILABLE_PATTERNS:
        raise HTTPException(status_code=404, detail="Pattern not found")
    
    # Placeholder - integrate actual pattern execution here
    return PatternRunResponse(
        pattern=pattern_name,
        input=request.input,
        output=f"Executed {pattern_name} with input: {request.input}"
    )

@router.get("/{pattern_name}")
def get_pattern_details(pattern_name: str):
    if pattern_name not in AVAILABLE_PATTERNS:
        raise HTTPException(status_code=404, detail="Pattern not found")
    
    return {
        "name": pattern_name,
        "description": f"{pattern_name} pattern implementation",
        "available": True
    }
