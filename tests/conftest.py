import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    earth = Planet(name="Earth",
                      description="home sweet home")
    saturn = Planet(name="Saturn",
                         description="I have rings")

    db.session.add_all([earth, saturn])
    db.session.commit()

@pytest.fixture
def one_planet(app): 
    return {
        "name": "Mars",
        "description": "another planet"
    }