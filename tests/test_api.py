from fastapi.testclient import TestClient

from financial_tools.api.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200



def test_ask():

    response = client.post(
        "/ask",
        json={
            "question":
            "Which invoice is pending?"
        }
    )

    assert response.status_code == 200

    assert "answer" in response.json()