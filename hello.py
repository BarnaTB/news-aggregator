from fastapi import Depends

from main.app import app
from main.config import get_settings, Settings

@app.get("/")
async def get(settings: Settings = Depends(get_settings)):
    return {
        "vibe ekutte": "Bandali Bandali eeh"
    }
