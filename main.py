from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)


app = FastAPI()


@app.post("/login")
async def login(email: str, password: str):
    response = supabase.auth.sign_in_with_password(
        {"email": email, "password": password}
    )
    return response


@app.post("/refresh_token")
async def refresh_token(refresh_token: str):
    response = supabase.auth.refresh_session(refresh_token)
    return response


@app.get("/protected")
async def protected(token: str):
    user = supabase.auth.get_user(token)
    if user.user is None:
        return {"error": "Invalid token"}
    return {"message": "Access granted", "user": user.user}
