from fastapi import APIRouter
from app.models.health import HealthResponse, ServiceHealthCheck, HealthStatus
from app.services.db.connection import check_mongo_connection
status_router = APIRouter()


@status_router.get("/all", response_model=HealthResponse)
async def get_status() -> HealthResponse:
    resp = HealthResponse()
    services = [
        await get_mongo_status()
    ]
    if any(service.status == HealthStatus.UNHEALTHY for service in services):
        resp.status = HealthStatus.UNHEALTHY
        resp.message = "One or more services are unhealthy."
    resp.services.append(*services)
    return resp


@status_router.get("/mongo-db", response_model=ServiceHealthCheck, description="Check if the database is reachable")
async def get_mongo_status() -> ServiceHealthCheck:
    service_name = "MongoDB"
    try:
        await check_mongo_connection()
        return ServiceHealthCheck(name=service_name)
    except Exception as e:
        return ServiceHealthCheck(name=service_name, status=HealthStatus.UNHEALTHY, error=str(e))
