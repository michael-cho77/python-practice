import os
from dotenv import load_dotenv
from pathlib import Path

# .env 파일 로드
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

MONGO_DATABASE = os.getenv("MONGO_DATABASE")
MONGO_URL = os.getenv("MONGO_URI")
