"""
Este archivo (app_test.py) contiene el test de la función para la 'app' blueprint.
"""


from project.app import app


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
