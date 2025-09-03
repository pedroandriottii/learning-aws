from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/auth/me")
async def auth_me(user: str = Body(None, embed=True)):
    return {"user": user or "anon", "ping": "pong"}
