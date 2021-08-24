from fastapi.testclient import TestClient
from app_python.api.server import app
import pytz
from datetime import datetime


client = TestClient(app)


def test_request():
    """Tests if endpoint is reachable and returning something"""
    response = client.get("/api/time/moscow")
    assert response.status_code == 200


def test_time():
    """Tests if the time is withing 5 seconds of the current server time in Moscow timezone"""
    response = client.get("/api/time/moscow")
    response_json = response.json()

    # time of the api
    response_datetime = datetime(response_json["year"], response_json["month"], response_json["day"],
                                 response_json["hour"], response_json["minute"], response_json["seconds"])

    tz = pytz.timezone('Europe/Moscow')
    # time of the server in Moscow timezone
    moscow_now = datetime.now(tz).replace(tzinfo=None)
    assert abs(response_datetime - moscow_now).total_seconds() <= 5
