import unittest
from unittest.mock import patch, MagicMock

from fastapi import HTTPException, Request
from fastapi.testclient import TestClient

from app.api.dependencies import verify_user
from app.schemas.user_schemas import UserBase
from app.utils.constants.error import BAD_CREDENTIALS, EMAIL_ALREADY_EXISTS
from main import app

client = TestClient(app)


# mocked get username function
async def mock_get_user_name(request: Request):
    request.state.user = UserBase(email="mock@gmail.com", full_name="Full Name Mock")


app.dependency_overrides[verify_user] = mock_get_user_name


class TestUserEndpoints(unittest.TestCase):
    @patch('app.api.endpoints.get_db')
    def test_login_admin(self, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db

        mock_login = MagicMock()
        mock_login.return_value = {"access_token": "mock_token"}
        with patch('app.api.endpoints.users_services.login', mock_login):
            user_data = {"email": "test@example.com", "password": "password123"}
            response = client.post("/users/login", json=user_data)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIn("access_token", response_data)
        self.assertEqual(response_data["access_token"], "mock_token")
        mock_login.assert_called_once()

    @patch('app.api.dependencies.get_db')
    def test_login_admin_failure(self, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db

        mock_login = MagicMock()
        mock_login.side_effect = HTTPException(status_code=500, detail={"code": BAD_CREDENTIALS})
        with patch('app.api.endpoints.users_services.login', mock_login):
            user_data = {"email": "test@example.com", "password": "password123"}
            response = client.post("/users/login", json=user_data)

        self.assertEqual(response.status_code, 500)

    def test_create_user(self):
        mock_login = MagicMock()
        mock_login.return_value = UserBase(email="test@example.com", full_name="test mock")
        with patch('app.api.endpoints.users_services.create_user', mock_login):
            user_data = {"email": "test@example.com", "password": "password123", "full_name": "test mock"}
            response = client.post("/users/", json=user_data, headers={"x-token": "mock_token"})

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("email", response_data)
        self.assertIn("full_name", response_data)
        self.assertEqual(response_data["email"], "test@example.com")
        self.assertEqual(response_data["full_name"], "test mock")

    def test_create_user_failure(self):
        mock_login = MagicMock()
        mock_login.side_effect = HTTPException(status_code=500, detail={"code": EMAIL_ALREADY_EXISTS})
        with patch('app.api.endpoints.users_services.create_user', mock_login):
            user_data = {"email": "test@example.com", "password": "password123", "full_name": "test mock"}
            response = client.post("/users/", json=user_data, headers={"x-token": "mock_token"})

        self.assertEqual(response.status_code, 500)
        response_data = response.json()
        self.assertIn("detail", response_data)
        self.assertIn("code", response_data["detail"])
        code = response_data["detail"]["code"]
        self.assertEqual(code, EMAIL_ALREADY_EXISTS)
