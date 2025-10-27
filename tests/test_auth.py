"""
Unit Tests for User Authentication Module
TC_001, TC_002, TC_003, TC_004, TC_005
"""
import pytest
from test_config import test_client, init_database
from main import User, db

class TestAuthentication:
    """Test cases for authentication module"""
    
    def test_signup_valid_data(self, test_client, init_database):
        """
        TC_001: Test user signup with valid data (Black-box, Positive)
        Expected: User registered successfully
        """
        with test_client.application.app_context():
            response = test_client.post('/signup', data={
                'username': 'testuser001',
                'email': 'testuser001@test.com',
                'password': 'password123'
            }, follow_redirects=True)
            
            # Check if user was created
            user = User.query.filter_by(email='testuser001@test.com').first()
            assert user is not None
            assert user.username == 'testuser001'
            assert response.status_code == 200
    
    def test_signup_duplicate_email(self, test_client, init_database):
        """
        TC_002: Test duplicate email prevention (Black-box, Negative)
        Expected: Registration fails with warning
        """
        with test_client.application.app_context():
            # Create a user first
            existing_user = User(username='existing', email='existing@test.com', password='pass')
            db.session.add(existing_user)
            db.session.commit()
            
            # Try to register with same email
            response = test_client.post('/signup', data={
                'username': 'newuser',
                'email': 'existing@test.com',
                'password': 'password123'
            })
            
            # Check if user was not created
            users = User.query.filter_by(email='existing@test.com').all()
            assert len(users) == 1
            assert response.status_code == 200
    
    def test_login_valid_credentials(self, test_client, init_database):
        """
        TC_003: Test login with valid credentials (Black-box, Positive)
        Expected: User logged in successfully
        """
        with test_client.application.app_context():
            # Create a test user
            test_user = User(username='logintest', email='login@test.com', password='testpass')
            db.session.add(test_user)
            db.session.commit()
            
            # Attempt login
            response = test_client.post('/login', data={
                'email': 'login@test.com',
                'password': 'testpass'
            }, follow_redirects=True)
            
            assert response.status_code == 200
            # Check that we're redirected to home
            assert b'index' in response.data or response.request.path == '/'
    
    def test_login_invalid_credentials(self, test_client, init_database):
        """
        TC_004: Test login with invalid credentials (Black-box, Negative)
        Expected: Login fails with error message
        """
        response = test_client.post('/login', data={
            'email': 'invalid@test.com',
            'password': 'wrongpassword'
        })
        
        assert response.status_code == 200
        # Should remain on login page
        assert b'login' in response.data.lower()
    
    def test_logout(self, test_client, init_database):
        """
        TC_005: Test logout functionality (Black-box, Positive)
        Expected: User logged out successfully
        """
        with test_client.application.app_context():
            # Create and login a user
            test_user = User(username='logouttest', email='logout@test.com', password='testpass')
            db.session.add(test_user)
            db.session.commit()
            
            # First login
            test_client.post('/login', data={
                'email': 'logout@test.com',
                'password': 'testpass'
            })
            
            # Then logout
            response = test_client.get('/logout', follow_redirects=True)
            
            assert response.status_code == 200
            # Should be redirected to login
            assert b'login' in response.data.lower() or response.request.path == '/login'

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
