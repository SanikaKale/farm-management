"""
Test configuration file
Provides test client and database setup
"""
import pytest
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app, db, User, Register, Farming, Addagroproducts, Trig
from flask_login import FlaskLoginClient

# Test database configuration
TEST_DB_URI = 'sqlite:///:memory:'

@pytest.fixture(scope='session')
def test_client():
    """Create test client"""
    # Configure test database
    app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    app.config['WTF_CSRF_ENABLED'] = False
    
    # Create test client
    client = app.test_client()
    client.testing = True
    
    return client

@pytest.fixture(scope='function')
def init_database(test_client):
    """Initialize test database"""
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Add sample data
        sample_user = User(username='testuser', email='test@test.com', password='password123')
        db.session.add(sample_user)
        
        sample_farming = Farming(farmingtype='Seed Farming')
        db.session.add(sample_farming)
        
        db.session.commit()
        
        yield db
        
        # Cleanup
        db.session.remove()
        db.drop_all()

@pytest.fixture
def authenticated_client(test_client):
    """Create authenticated test client"""
    client = test_client
    app.test_client_class = FlaskLoginClient
    
    return client
