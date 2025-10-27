"""
Unit Tests for Farmer Management Module
TC_006, TC_007, TC_008, TC_009, TC_010
"""
import pytest
from test_config import test_client, init_database
from main import User, Register, Farming, db
from flask_login import FlaskLoginClient, login_user

class TestFarmerManagement:
    """Test cases for farmer management"""
    
    @pytest.fixture
    def logged_in_client(self, test_client, init_database):
        """Create a logged-in test client"""
        with test_client.application.app_context():
            # Create a user for testing
            test_user = User(username='farmeruser', email='farmer@test.com', password='testpass')
            db.session.add(test_user)
            db.session.commit()
            
            # Login the user
            with test_client.session_transaction() as sess:
                login_user(test_user)
            
            return test_client
    
    def test_add_farmer_valid_data(self, logged_in_client, init_database):
        """
        TC_006: Test adding farmer with valid data (Black-box, Positive)
        Expected: Farmer added successfully
        """
        with logged_in_client.application.app_context():
            # Add a farming type first
            farming = Farming(farmingtype='Seed Farming')
            db.session.add(farming)
            db.session.commit()
            
            response = logged_in_client.post('/register', data={
                'farmername': 'John Doe',
                'adharnumber': '123456789012',
                'age': '35',
                'gender': 'Male',
                'phonenumber': '9876543210',
                'address': '123 Main Street',
                'farmingtype': 'Seed Farming'
            }, follow_redirects=True)
            
            # Check if farmer was created
            farmer = Register.query.filter_by(farmername='John Doe').first()
            assert farmer is not None
            assert farmer.age == 35
            assert response.status_code == 200
    
    def test_view_farmer_list(self, logged_in_client, init_database):
        """
        TC_008: Test viewing farmer list (Black-box, Positive)
        Expected: Farmer list displayed
        """
        with logged_in_client.application.app_context():
            # Create sample farmers
            farmer1 = Register(
                farmername='Test Farmer 1',
                adharnumber='123456789012',
                age=35,
                gender='Male',
                phonenumber='9876543210',
                address='Address 1',
                farming='Seed Farming'
            )
            farmer2 = Register(
                farmername='Test Farmer 2',
                adharnumber='123456789013',
                age=40,
                gender='Female',
                phonenumber='9876543211',
                address='Address 2',
                farming='Seed Farming'
            )
            db.session.add(farmer1)
            db.session.add(farmer2)
            db.session.commit()
            
            response = logged_in_client.get('/farmerdetails')
            
            assert response.status_code == 200
            assert b'Test Farmer 1' in response.data
            assert b'Test Farmer 2' in response.data
    
    def test_edit_farmer_details(self, logged_in_client, init_database):
        """
        TC_009: Test editing farmer details (Black-box, Positive)
        Expected: Farmer details updated successfully
        """
        with logged_in_client.application.app_context():
            # Create a farmer
            farmer = Register(
                farmername='Original Name',
                adharnumber='123456789012',
                age=35,
                gender='Male',
                phonenumber='9876543210',
                address='Original Address',
                farming='Seed Farming'
            )
            db.session.add(farmer)
            db.session.commit()
            
            # Add farming type
            farming = Farming(farmingtype='Seed Farming')
            db.session.add(farming)
            db.session.commit()
            
            # Edit the farmer
            response = logged_in_client.post(f'/edit/{farmer.rid}', data={
                'farmername': 'Updated Name',
                'adharnumber': '123456789012',
                'age': '40',
                'gender': 'Male',
                'phonenumber': '9876543210',
                'address': 'Updated Address',
                'farmingtype': 'Seed Farming'
            }, follow_redirects=True)
            
            # Verify update
            updated_farmer = Register.query.get(farmer.rid)
            assert updated_farmer.farmername == 'Updated Name'
            assert updated_farmer.age == 40
            assert response.status_code == 200
    
    def test_delete_farmer(self, logged_in_client, init_database):
        """
        TC_010: Test deleting farmer (Black-box, Positive)
        Expected: Farmer deleted successfully
        """
        with logged_in_client.application.app_context():
            # Create a farmer
            farmer = Register(
                farmername='To Be Deleted',
                adharnumber='123456789012',
                age=35,
                gender='Male',
                phonenumber='9876543210',
                address='Some Address',
                farming='Seed Farming'
            )
            db.session.add(farmer)
            db.session.commit()
            farmer_id = farmer.rid
            
            # Delete the farmer
            response = logged_in_client.post(f'/delete/{farmer_id}', follow_redirects=True)
            
            # Verify deletion
            deleted_farmer = Register.query.get(farmer_id)
            assert deleted_farmer is None
            assert response.status_code == 200

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
