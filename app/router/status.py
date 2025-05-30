from fastapi import APIRouter
from app.models.health import HealthResponse

status_router = APIRouter()


@status_router.get("/health", response_model=HealthResponse)
async def get_status() -> HealthResponse:
    # TODO: Implement actual health check logic
    return HealthResponse()
