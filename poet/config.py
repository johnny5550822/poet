import os
from dotenv import load_dotenv

load_dotenv()

# Default to 1.5-flash if the .env variable is missing
MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")