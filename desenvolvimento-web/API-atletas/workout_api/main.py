from fastapi import FastAPI
from workout_api.routers import api_router
from fastapi_pagination import add_pagination

app = FastAPI(title="WorkoutApi")

add_pagination(app)

app.include_router(api_router)

if __name__ == "main":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
