"""
Test cases for Contact Management System
CS1350 Week 1 Homework
"""

import contact_manager as cm
import datetime

def test_create_contact():
    """Test contact creation with valid and invalid data."""
    print("Testing create_contact()...")
    
    # Test with valid data
    print("1. Testing with valid data...")
    contact_data = {
        'first_name': 'Test',
        'last_name': 'User',
        'phone': '123-456-7890',
        'email': 'test@example.com',
        'address': {
            'street': '123 Test St',
            'city': 'Testville',
            'state': 'TS',
            'zip_code': '12345'
        },
        'category': 'personal',
        'notes': 'Test contact',
        'created_date': '2024-01-15',
        'last_modified': '2024-01-15'
    }
    
    # Simulate creating a contact
    contact_id = cm.add_contact(cm.contacts_db, contact_data)
    assert contact_id is not None
    assert contact_id in cm.contacts_db
    print("   ✓ Valid contact created successfully")
    
    # Test with invalid phone
    print("2. Testing with invalid phone...")
    invalid_contact = contact_data.copy()
    invalid_contact['phone'] = 'invalid-phone'
    result = cm.add_contact(cm.contacts_db, invalid_contact)
    assert result is None
    print("   ✓ Invalid phone correctly rejected")
    
    print("create_contact() tests passed!\n")

def test_search_functionality():
    """Test all search functions with various scenarios."""
    print("Testing search functionality...")
    
    # Add some test contacts
    contact1 = {
        'first_name': 'Alice',
        'last_name': 'Johnson',
        'phone': '111-222-3333',
        'email': 'alice@example.com',
        'category': 'work',
        'notes': '',
        'created_date': '2024-01-15',
        'last_modified': '2024-01-15'
    }
    
    contact2 = {
        'first_name': 'Bob',
        'last_name': 'Smith',
        'phone': '444-555-6666',
        'email': 'bob@example.com',
        'category': 'personal',
        'notes': '',
        'created_date': '2024-01-16',
        'last_modified': '2024-01-16'
    }
    
    contact3 = {
        'first_name': 'Carol',
        'last_name': 'Johnson',
        'phone': '777-888-9999',
        'email': 'carol@example.com',
        'category': 'work',
        'notes': '',
        'created_date': '2024-01-17',
        'last_modified': '2024-01-17'
    }
    
    cm.contacts_db.clear()
    id1 = cm.add_contact(cm.contacts_db, contact1)
    id2 = cm.add_contact(cm.contacts_db, contact2)
    id3 = cm.add_contact(cm.contacts_db, contact3)
    
    # Test name search
    results = cm.search_contacts_by_name(cm.contacts_db, 'johnson')
    assert len(results) == 2
    assert id1 in results and id3 in results
    print("   ✓ Name search works correctly")
    
    # Test category search
    results = cm.search_contacts_by_category(cm.contacts_db, 'work')
    assert len(results) == 2
    assert id1 in results and id3 in results
    print("   ✓ Category search works correctly")
    
    # Test phone search
    contact_id, contact_data = cm.find_contact_by_phone(cm.contacts_db, '444-555-6666')
    assert contact_id == id2
    print("   ✓ Phone search works correctly")
    
    print("Search functionality tests passed!\n")

def test_contact_operations():
    """Test add, update, delete operations."""
    print("Testing contact operations...")
    
    cm.contacts_db.clear()
    
    # Test add
    contact_data = {
        'first_name': 'Test',
        'last_name': 'User',
        'phone': '123-456-7890',
        'email': 'test@example.com',
        'category': 'personal',
        'notes': '',
        'created_date': '2024-01-15',
        'last_modified': '2024-01-15'
    }
    
    contact_id = cm.add_contact(cm.contacts_db, contact_data)
    assert contact_id in cm.contacts_db
    print("   ✓ Contact addition works correctly")
    
    # Test update
    updates = {'first_name': 'Updated', 'last_name': 'Name'}
    success = cm.update_contact(cm.contacts_db, contact_id, updates)
    assert success
    assert cm.contacts_db[contact_id]['first_name'] == 'Updated'
    assert cm.contacts_db[contact_id]['last_name'] == 'Name'
    print("   ✓ Contact update works correctly")
    
    # Test delete
    success = cm.delete_contact(cm.contacts_db, contact_id)
    assert success
    assert contact_id not in cm.contacts_db
    print("   ✓ Contact deletion works correctly")
    
    print("Contact operations tests passed!\n")

def test_data_analysis():
    """Test statistics and duplicate detection."""
    print("Testing data analysis...")
    
    cm.contacts_db.clear()
    
    # Add test contacts
    contacts = [
        {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'phone': '111-222-3333',
            'email': 'alice@example.com',
            'address': {'state': 'CA'},
            'category': 'work',
            'notes': '',
            'created_date': '2024-01-15',
            'last_modified': '2024-01-15'
        },
        {
            'first_name': 'Bob',
            'last_name': 'Smith',
            'phone': '111-222-4444',  # Same area code as Alice
            'email': 'bob@example.com',
            'address': {'state': 'NY'},
            'category': 'personal',
            'notes': '',
            'created_date': '2024-01-16',
            'last_modified': '2024-01-16'
        },
        {
            'first_name': 'Alice',
            'last_name': 'Johnson',  # Same name as first contact
            'phone': '555-666-7777',
            'email': 'alice.j@example.com',  # Different email
            'category': 'work',
            'notes': '',
            'created_date': '2024-01-17',
            'last_modified': '2024-01-17'
        }
    ]
    
    for contact in contacts:
        cm.add_contact(cm.contacts_db, contact)
    
    # Test statistics
    stats = cm.generate_contact_statistics(cm.contacts_db)
    assert stats['total_contacts'] == 3
    assert stats['contacts_by_category']['work'] == 2
    assert stats['contacts_by_category']['personal'] == 1
    assert stats['most_common_area_code'] == '111'
    print("   ✓ Statistics generation works correctly")
    
    # Test duplicate detection
    duplicates = cm.find_duplicate_contacts(cm.contacts_db)
    assert len(duplicates['name_duplicates']) == 1  # Two Alice Johnsons
    print("   ✓ Duplicate detection works correctly")
    
    print("Data analysis tests passed!\n")

def test_validation_functions():
    """Test phone and email validation."""
    print("Testing validation functions...")
    
    # Test phone validation
    assert cm.validate_phone('123-456-7890') == True
    assert cm.validate_phone('1234567890') == False
    assert cm.validate_phone('123-456-789') == False
    assert cm.validate_phone('abc-def-ghij') == False
    print("   ✓ Phone validation works correctly")
    
    # Test email validation
    assert cm.validate_email('test@example.com') == True
    assert cm.validate_email('test.example.com') == False
    assert cm.validate_email('test@example') == False
    assert cm.validate_email('@example.com') == False
    print("   ✓ Email validation works correctly")
    
    print("Validation tests passed!\n")

def run_all_tests():
    """Run all test functions and report results."""
    print("Running all tests for Contact Management System...\n")
    
    # Reset the contacts database before testing
    cm.contacts_db = {}
    
    try:
        test_validation_functions()
        test_create_contact()
        test_search_functionality()
        test_contact_operations()
        test_data_analysis()
        
        print("All tests passed! ✅")
        return True
    except Exception as e:
        print(f"Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    run_all_tests()