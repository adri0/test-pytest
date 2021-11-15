import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print("Setting up db...")
    pass