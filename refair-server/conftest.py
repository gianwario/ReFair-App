import pytest
from app import app as refair


@pytest.fixture()
def app():
    refair.config.update({
        "TESTING": True,
    })

    yield refair


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
