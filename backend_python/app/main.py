from fastapi import FastAPI
from app.routes.password_routes import router as password_router

app = FastAPI(
    title="PassML API",
    version="0.1.0"
)

@app.get("/")
def root():
    return{"message":"PassML_API is running"}

app.include_router(password_router)