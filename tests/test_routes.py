def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_with_no_records(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404

def test_get_all_planets(client, two_saved_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == [
        {"id": 1,
        "name": "Earth",
        "description": "home sweet home"}, 
        {"id": 2,
        "name": "Saturn",
        "description": "I have rings"}]

def test_post_one_book(client, one_planet):
    #Act
    response = client.post("/planets", json=one_planet)
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    # assert response_body == (f"Planet {one_planet['name']} successfully created")
    assert response_body == {
            "message": "Planet successfully created"
        }