from fastapi import FastAPI
from typing import Optional

from src.application.controllers import health_check_controller


def create_app(additional_settings: Optional[dict] = None) -> FastAPI:
    app = FastAPI(
        title="Tax API",
        description="API que oferece serviços relacionados à tributação",
        version="1.0.0",
        contact={
            "name": "Gabriel Ladeira",
            "url": "https://www.linkedin.com/in/g-ladeira/",
            "email": "gabrielxladeira@gmail.com",
        },
        **additional_settings,
    )

    app.include_router(health_check_controller.router)

    return app


app = create_app(additional_settings={"debug": True})
