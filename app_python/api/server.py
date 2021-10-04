from fastapi import FastAPI
from .routes import router as api_router
from app_python.core.tasks import create_start_app_handler, create_stop_app_handler


def get_app():
    """Function creates app with all the routes and settings we need"""
    app = FastAPI()

    # start and shutdown event handlers
    app.add_event_handler("startup", create_start_app_handler(app))
    app.add_event_handler("shutdown", create_stop_app_handler(app))

    # include all routes
    app.include_router(api_router, prefix="")
    return app


# Create app
app = get_app()
