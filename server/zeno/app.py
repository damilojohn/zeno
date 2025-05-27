from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from zeno.api.v2.endpoints.endpoints import router
import uvicorn
import structlog

LOG = structlog.stdlib.get_logger()


app = FastAPI(title="Zeno's Backend")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


if __name__ == "__main__":
    LOG.info("server starting.....", host="0.0.0.0")
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        log_level="info",
        port=8000,
        reload=True
    )
