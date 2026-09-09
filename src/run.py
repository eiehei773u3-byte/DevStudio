from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import ollama
from fastapi.responses import StreamingResponse
import uvicorn

app = FastAPI(title="DevStudio")

# ... остальной код