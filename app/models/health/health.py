from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timezone


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"


class ServiceHealthCheck(BaseModel):
    name: str = Field(..., description="Name of the service")
    status: HealthStatus = Field(default=HealthStatus.HEALTHY)
    error: str | None = Field(
        default=None, description="Error message if the service is unhealthy"
    )


class HealthResponse(BaseModel):
    status: HealthStatus = Field(default=HealthStatus.HEALTHY)
    message: str = Field(default="The API is running smoothly.")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    services: list[ServiceHealthCheck] = Field(
        default_factory=list, description="List of services and their health status"
    )
