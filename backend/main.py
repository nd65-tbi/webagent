from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

print("✅ FastAPI app is loading...")

app = FastAPI(
    title="WebAgent API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    email: str
    password: str

@app.get("/")
def root():
    return {"message": "Backend is running!"}

@app.post("/login")
def login(data: LoginData):
    if data.email == "admin@example.com" and data.password == "password":
        return {"token": "example_token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
