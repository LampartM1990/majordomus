import uvicorn
from app.app_config import Config

config = Config()

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=config.api.PORT,
        reload=config.environment == "development",
    )
