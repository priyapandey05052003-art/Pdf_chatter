from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
VOYAGE_API_KEY=os.getenv("VOYAGE_API_KEY","")
GROQ_API_KEY=os.getenv("GROQ_API_KEY","")

