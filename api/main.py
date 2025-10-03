from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import patterns, health
from api.middleware.logging import LoggingMiddleware
import os

app = FastAPI(
    title="AWS Agentic Architectures API",
    description="REST API for 17 agentic patterns built on AWS Bedrock",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("API_CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom logging middleware
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(health.router)
app.include_router(patterns.router)

@app.get("/")
def read_root():
    return {
        "message": "AWS Agentic Architectures API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
