from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timezone


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"


class UnhealthyReason(str, Enum):
    UNKNOWN = "unknown"


class HealthResponse(BaseModel):
    status: HealthStatus = Field(default=HealthStatus.HEALTHY)
    message: str = Field(default="The API is running smoothly.")
    timestamp: datetime = Field(default=datetime.now(timezone.utc))
    unhealthy_reason: UnhealthyReason | None = Field(
        default=None, description="Reason for unhealthiness if status is UNHEALTHY"
    )
