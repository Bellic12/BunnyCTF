from fastapi import FastAPI

app = FastAPI()


# Simple health check endpoint to verify the server is running
@app.get("/health")
def health_check():
    return {"status": "ok"}
