from fastapi import FastAPI
from typing import Callable


def create_start_app_handler(app: FastAPI) -> Callable:
    """Task that will be performed after the start of the server (currently nothing, but can be useful)"""
    async def start_app() -> None:
        pass
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    """Task that will be performed before the finish of the server (currently nothing, but can be useful)"""
    async def stop_app() -> None:
        pass
    return stop_app
