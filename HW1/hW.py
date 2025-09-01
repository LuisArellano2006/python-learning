"""
CS1350 Week 1 Homework: Dictionary Operations
"""

import datetime
import re
from collections import defaultdict

# Contact database structure
contacts_db = {}

def create_contact():
    """
    Create a new contact dictionary by prompting for user input.
    
    Returns:
        dict: A properly formatted contact dictionary, or None if creation failed
    """
    print("\n--- Create New Contact ---")
    
    # Required fields with validation
    first_name = input("First Name: ").strip()
    if not first_name:
        print("Error: First name is required.")
        return None
        
    last_name = input("Last Name: ").strip()
    if not last_name:
        print("Error: Last name is required.")
        return None
        
    phone = input("Phone (format: XXX-XXX-XXXX): ").strip()
    if not validate_phone(phone):
        print("Error: Valid phone number is required (format: XXX-XXX-XXXX).")
        return None
    
    # Optional fields
    email = input("Email: ").strip()
    if email and not validate_email(email):
        print("Warning: Email format appears invalid. Saving anyway.")
    
    # Address components
    street = input("Street Address: ").strip()
    city = input("City: ").strip()
    state = input("State (2-letter code): ").strip().upper()
    zip_code = input("ZIP Code: ").strip()
    
    category = input("Category (personal, work, family): ").strip().lower()
    if category not in ['personal', 'work', 'family']:
        category = 'personal'  # Default category
        
    notes = input("Notes: ").strip()
    
    # Create address dictionary if any address component is provided
    address = {}
    if any([street, city, state, zip_code]):
        address = {
            'street': street,
            'city': city,
            'state': state if len(state) == 2 else '',
            'zip_code': zip_code
        }
    
    # Current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Build contact dictionary
    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email if email else '',
        'address': address,
        'category': category,
        'notes': notes if notes else '',
        'created_date': current_time,
        'last_modified': current_time
    }
    
    return contact

def validate_phone(phone):
    """
    Validate phone number format (XXX-XXX-XXXX).
    
    Args:
        phone (str): Phone number to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None

def validate_email(email):
    """
    Basic email validation.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid format, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_contact_id(contacts_db):
    """
    Generate a unique contact ID.
    
    Args:
        contacts_db (dict): The contacts database
        
    Returns:
        str: A unique contact ID
    """
    if not contacts_db:
        return 'contact_001'
    
    # Find the highest existing ID and increment
    max_id = max(contacts_db.keys(), key=lambda x: int(x.split('_')[1]))
    max_num = int(max_id.split('_')[1])
    return f'contact_{max_num + 1:03d}'

def add_contact(contacts_db, contact_data):
    """
    Add a new contact to the database.
    
    Args:
        contacts_db (dict): The main contacts database
        contact_data (dict): Contact information dictionary
        
    Returns:
        str: The generated contact ID, or None if addition failed
    """
    if not contact_data:
        return None
        
    contact_id = generate_contact_id(contacts_db)
    contacts_db[contact_id] = contact_data
    return contact_id

def display_contact(contacts_db, contact_id):
    """
    Display a formatted view of a single contact.
    
    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Unique identifier for the contact
        
    Returns:
        bool: True if contact found and displayed, False otherwise
    """
    if contact_id not in contacts_db:
        print(f"Contact with ID {contact_id} not found.")
        return False
        
    contact = contacts_db[contact_id]
    
    print(f"\n--- Contact: {contact_id} ---")
    print(f"Name: {contact['first_name']} {contact['last_name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    
    if contact['address']:
        print("Address:")
        addr = contact['address']
        if addr['street']:
            print(f"  Street: {addr['street']}")
        if addr['city']:
            print(f"  City: {addr['city']}")
        if addr['state']:
            print(f"  State: {addr['state']}")
        if addr['zip_code']:
            print(f"  ZIP: {addr['zip_code']}")
    
    print(f"Category: {contact['category']}")
    if contact['notes']:
        print(f"Notes: {contact['notes']}")
    
    print(f"Created: {contact['created_date']}")
    print(f"Last Modified: {contact['last_modified']}")
    
    return True

def list_all_contacts(contacts_db):
    """
    Display a summary list of all contacts (ID, name, phone).
    
    Args:
        contacts_db (dict): The main contacts database
    """
    if not contacts_db:
        print("No contacts in database.")
        return
        
    print("\n--- All Contacts ---")
    for contact_id, contact in contacts_db.items():
        print(f"{contact_id}: {contact['first_name']} {contact['last_name']} - {contact['phone']}")

def search_contacts_by_name(contacts_db, search_term):
    """
    Search contacts by first or last name (case-insensitive partial match).
    
    Args:
        contacts_db (dict): The main contacts database
        search_term (str): Name to search for
        
    Returns:
        dict: Dictionary of matching contacts (contact_id: contact_data)
    """
    results = {}
    search_term = search_term.lower()
    
    for contact_id, contact in contacts_db.items():
        first_name = contact['first_name'].lower()
        last_name = contact['last_name'].lower()
        
        if search_term in first_name or search_term in last_name:
            results[contact_id] = contact
            
    return results

def search_contacts_by_category(contacts_db, category):
    """
    Find all contacts in a specific category.
    
    Args:
        contacts_db (dict): The main contacts database
        category (str): Category to filter by
        
    Returns:
        dict: Dictionary of matching contacts
    """
    results = {}
    category = category.lower()
    
    for contact_id, contact in contacts_db.items():
        if contact['category'].lower() == category:
            results[contact_id] = contact
            
    return results

def find_contact_by_phone(contacts_db, phone_number):
    """
    Find contact by phone number (exact match).
    
    Args:
        contacts_db (dict): The main contacts database
        phone_number (str): Phone number to search for
        
    Returns:
        tuple: (contact_id, contact_data) if found, (None, None) if not found
    """
    for contact_id, contact in contacts_db.items():
        if contact['phone'] == phone_number:
            return (contact_id, contact)
            
    return (None, None)

def update_contact(contacts_db, contact_id, field_updates):
    """
    Update specific fields of an existing contact.
    Automatically update last modified timestamp.
    
    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Contact to update
        field_updates (dict): Dictionary of fields to update
        
    Returns:
        bool: True if update successful, False otherwise
    """
    if contact_id not in contacts_db:
        print(f"Contact with ID {contact_id} not found.")
        return False
        
    # Validate phone if being updated
    if 'phone' in field_updates and not validate_phone(field_updates['phone']):
        print("Error: Invalid phone format. Update cancelled.")
        return False
        
    # Validate email if being updated
    if 'email' in field_updates and field_updates['email'] and not validate_email(field_updates['email']):
        print("Warning: Email format appears invalid. Continuing anyway.")
    
    # Update the fields
    for field, value in field_updates.items():
        if field == 'address':
            # Handle address updates
            if 'address' not in contacts_db[contact_id]:
                contacts_db[contact_id]['address'] = {}
                
            for addr_field, addr_value in value.items():
                contacts_db[contact_id]['address'][addr_field] = addr_value
        else:
            contacts_db[contact_id][field] = value
    
    # Update last modified timestamp
    contacts_db[contact_id]['last_modified'] = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return True

def delete_contact(contacts_db, contact_id):
    """
    Remove a contact from the database with confirmation.
    
    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Contact to delete
        
    Returns:
        bool: True if deletion successful, False otherwise
    """
    if contact_id not in contacts_db:
        print(f"Contact with ID {contact_id} not found.")
        return False
        
    # Display contact before deletion
    display_contact(contacts_db, contact_id)
    
    # Confirmation
    confirm = input(f"\nAre you sure you want to delete contact {contact_id}? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return False
        
    del contacts_db[contact_id]
    print(f"Contact {contact_id} deleted successfully.")
    return True

def merge_contacts(contacts_db, contact_id1, contact_id2):
    """
    Merge two contacts, keeping the most recent information.
    Prompt user for conflicts in overlapping fields.
    
    Args:
        contacts_db (dict): The main contacts database
        contact_id1 (str): First contact ID
        contact_id2 (str): Second contact ID
        
    Returns:
        str: ID of the merged contact, or None if merge failed
    """
    if contact_id1 not in contacts_db or contact_id2 not in contacts_db:
        print("One or both contact IDs not found.")
        return None
        
    contact1 = contacts_db[contact_id1]
    contact2 = contacts_db[contact_id2]
    
    print(f"\nMerging contacts:")
    print(f"1. {contact_id1}: {contact1['first_name']} {contact1['last_name']}")
    print(f"2. {contact_id2}: {contact2['first_name']} {contact2['last_name']}")
    
    # Create a new merged contact
    merged_contact = {}
    
    # For each field, decide which value to keep
    all_fields = set(contact1.keys()) | set(contact2.keys())
    
    for field in all_fields:
        if field not in contact1:
            merged_contact[field] = contact2[field]
        elif field not in contact2:
            merged_contact[field] = contact1[field]
        else:
            # Both contacts have this field
            if field in ['created_date', 'last_modified']:
                # For dates, keep the most recent
                date1 = datetime.datetime.strptime(contact1[field], "%Y-%m-%d")
                date2 = datetime.datetime.strptime(contact2[field], "%Y-%m-%d")
                merged_contact[field] = contact1[field] if date1 > date2 else contact2[field]
            elif field == 'address':
                # Merge addresses
                merged_address = {}
                addr1 = contact1.get('address', {})
                addr2 = contact2.get('address', {})
                
                addr_fields = set(addr1.keys()) | set(addr2.keys())
                for addr_field in addr_fields:
                    if addr_field not in addr1:
                        merged_address[addr_field] = addr2[addr_field]
                    elif addr_field not in addr2:
                        merged_address[addr_field] = addr1[addr_field]
                    else:
                        # Both addresses have this field
                        if addr1[addr_field] and not addr2[addr_field]:
                            merged_address[addr_field] = addr1[addr_field]
                        elif addr2[addr_field] and not addr1[addr_field]:
                            merged_address[addr_field] = addr2[addr_field]
                        else:
                            # Both have values - prompt user
                            print(f"\nAddress field conflict: {addr_field}")
                            print(f"1. {addr1[addr_field]}")
                            print(f"2. {addr2[addr_field]}")
                            choice = input("Which value to keep? (1/2): ").strip()
                            merged_address[addr_field] = addr1[addr_field] if choice == '1' else addr2[addr_field]
                
                merged_contact[field] = merged_address
            else:
                # For other fields, prompt user to choose
                print(f"\nField conflict: {field}")
                print(f"1. {contact1[field]}")
                print(f"2. {contact2[field]}")
                choice = input("Which value to keep? (1/2): ").strip()
                merged_contact[field] = contact1[field] if choice == '1' else contact2[field]
    
    # Add the merged contact
    new_contact_id = add_contact(contacts_db, merged_contact)
    
    # Delete the original contacts
    del contacts_db[contact_id1]
    del contacts_db[contact_id2]
    
    print(f"Contacts merged successfully. New contact ID: {new_contact_id}")
    return new_contact_id

def generate_contact_statistics(contacts_db):
    """
    Generate comprehensive statistics about the contact database.
    
    Args:
        contacts_db (dict): The main contacts database
        
    Returns:
        dict: Statistics including:
        - total_contacts: int
        - contacts_by_category: dict
        - contacts_by_state: dict (from address)
        - average_contacts_per_category: float
        - most_common_area_code: str
        - contacts_without_email: int
    """
    stats = {
        'total_contacts': len(contacts_db),
        'contacts_by_category': defaultdict(int),
        'contacts_by_state': defaultdict(int),
        'contacts_without_email': 0,
        'area_codes': defaultdict(int)
    }
    
    # Count contacts by category and state
    for contact in contacts_db.values():
        stats['contacts_by_category'][contact['category']] += 1
        
        # Count contacts without email
        if not contact['email']:
            stats['contacts_without_email'] += 1
            
        # Extract area code from phone
        if contact['phone']:
            area_code = contact['phone'].split('-')[0]
            stats['area_codes'][area_code] += 1
            
        # Count by state if address exists
        if contact.get('address') and contact['address'].get('state'):
            stats['contacts_by_state'][contact['address']['state']] += 1
    
    # Calculate average contacts per category
    if stats['contacts_by_category']:
        stats['average_contacts_per_category'] = (
            len(contacts_db) / len(stats['contacts_by_category']))
    else:
        stats['average_contacts_per_category'] = 0
    
    # Find most common area code
    if stats['area_codes']:
        stats['most_common_area_code'] = max(
            stats['area_codes'].items(), key=lambda x: x[1])[0]
    else:
        stats['most_common_area_code'] = 'N/A'
    
    # Convert defaultdicts to regular dicts for cleaner output
    stats['contacts_by_category'] = dict(stats['contacts_by_category'])
    stats['contacts_by_state'] = dict(stats['contacts_by_state'])
    
    return stats

def find_duplicate_contacts(contacts_db):
    """
    Identify potential duplicate contacts based on:
    - Same phone number
    - Same email address
    - Same first+last name combination
    
    Args:
        contacts_db (dict): The main contacts database
        
    Returns:
        dict: Dictionary with duplicate types as keys and lists of contact IDs as values
    """
    duplicates = {
        'phone_duplicates': defaultdict(list),
        'email_duplicates': defaultdict(list),
        'name_duplicates': defaultdict(list)
    }
    
    # Create mappings for each duplicate type
    for contact_id, contact in contacts_db.items():
        # Phone duplicates
        if contact['phone']:
            duplicates['phone_duplicates'][contact['phone']].append(contact_id)
        
        # Email duplicates (only if email exists)
        if contact['email']:
            duplicates['email_duplicates'][contact['email']].append(contact_id)
        
        # Name duplicates
        name_key = f"{contact['first_name'].lower()} {contact['last_name'].lower()}"
        duplicates['name_duplicates'][name_key].append(contact_id)
    
    # Filter out non-duplicates (only keep entries with 2+ contacts)
    result = {}
    for dup_type, dup_dict in duplicates.items():
        result[dup_type] = [
            contact_ids for contact_ids in dup_dict.values() 
            if len(contact_ids) > 1
        ]
    
    return result

def export_contacts_by_category(contacts_db, category):
    """
    Export contacts from a specific category as a formatted string.
    Include all contact information in a readable format.
    
    Args:
        contacts_db (dict): The main contacts database
        category (str): Category to export
        
    Returns:
        str: Formatted string representation of all contacts in category
    """
    category_contacts = search_contacts_by_category(contacts_db, category)
    
    if not category_contacts:
        return f"No contacts found in category '{category}'."
    
    output = f"--- Contacts in Category: {category} ---\n\n"
    
    for contact_id, contact in category_contacts.items():
        output += f"Contact ID: {contact_id}\n"
        output += f"Name: {contact['first_name']} {contact['last_name']}\n"
        output += f"Phone: {contact['phone']}\n"
        output += f"Email: {contact['email']}\n"
        
        if contact['address']:
            output += "Address:\n"
            addr = contact['address']
            if addr['street']:
                output += f"  Street: {addr['street']}\n"
            if addr['city']:
                output += f"  City: {addr['city']}\n"
            if addr['state']:
                output += f"  State: {addr['state']}\n"
            if addr['zip_code']:
                output += f"  ZIP: {addr['zip_code']}\n"
        
        output += f"Category: {contact['category']}\n"
        if contact['notes']:
            output += f"Notes: {contact['notes']}\n"
        
        output += f"Created: {contact['created_date']}\n"
        output += f"Last Modified: {contact['last_modified']}\n"
        output += "-" * 40 + "\n\n"
    
    return output

def save_contacts_to_file(contacts_db, filename):
    """
    Save contacts database to a text file in a readable format.
    
    Args:
        contacts_db (dict): The contacts database
        filename (str): The filename to save to
    """
    try:
        with open(filename, 'w') as f:
            for contact_id, contact in contacts_db.items():
                f.write(f"=== {contact_id} ===\n")
                for key, value in contact.items():
                    if key == 'address':
                        f.write("address:\n")
                        for addr_key, addr_value in value.items():
                            f.write(f"  {addr_key}: {addr_value}\n")
                    else:
                        f.write(f"{key}: {value}\n")
                f.write("\n")
        print(f"Contacts saved to {filename} successfully.")
        return True
    except IOError as e:
        print(f"Error saving to file: {e}")
        return False

def load_contacts_from_file(filename):
    """
    Load contacts database from a text file.
    Return empty dict if file doesn't exist.
    
    Args:
        filename (str): The filename to load from
        
    Returns:
        dict: The loaded contacts database
    """
    contacts_db = {}
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        current_contact_id = None
        current_contact = {}
        in_address = False
        current_address = {}
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('===') and line.endswith('==='):
                # Save previous contact if exists
                if current_contact_id and current_contact:
                    if current_address:
                        current_contact['address'] = current_address
                    contacts_db[current_contact_id] = current_contact
                
                # Start new contact
                current_contact_id = line[4:-4].strip()  # Extract ID from === ID ===
                current_contact = {}
                current_address = {}
                in_address = False
                
            elif line == 'address:':
                in_address = True
                
            elif in_address and line.startswith('  '):
                # Address field
                if ': ' in line[2:]:
                    key, value = line[2:].split(': ', 1)
                    current_address[key] = value
                    
            elif ': ' in line:
                # Regular field
                key, value = line.split(': ', 1)
                current_contact[key] = value
                in_address = False
                
        # Save the last contact
        if current_contact_id and current_contact:
            if current_address:
                current_contact['address'] = current_address
            contacts_db[current_contact_id] = current_contact
            
        print(f"Contacts loaded from {filename} successfully.")
        return contacts_db
        
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty database.")
        return {}
    except Exception as e:
        print(f"Error loading from file: {e}")
        return {}

def main_menu():
    """
    Display and handle the main menu for the contact management system.
    """
    global contacts_db
    
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add new contact")
        print("2. Search contacts")
        print("3. List all contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Merge contacts")
        print("7. Generate statistics")
        print("8. Find duplicates")
        print("9. Export by category")
        print("10. Save to file")
        print("11. Load from file")
        print("12. Exit")
        
        choice = input("\nEnter your choice (1-12): ").strip()
        
        if choice == '1':
            # Add new contact
            contact_data = create_contact()
            if contact_data:
                contact_id = add_contact(contacts_db, contact_data)
                print(f"Contact added successfully with ID: {contact_id}")
                
        elif choice == '2':
            # Search contacts
            print("\nSearch options:")
            print("1. By name")
            print("2. By category")
            print("3. By phone")
            
            search_choice = input("Enter search option (1-3): ").strip()
            
            if search_choice == '1':
                name = input("Enter name to search: ").strip()
                results = search_contacts_by_name(contacts_db, name)
                if results:
                    print(f"\nFound {len(results)} matching contacts:")
                    for contact_id in results:
                        display_contact(contacts_db, contact_id)
                else:
                    print("No contacts found with that name.")
                    
            elif search_choice == '2':
                category = input("Enter category to search: ").strip()
                results = search_contacts_by_category(contacts_db, category)
                if results:
                    print(f"\nFound {len(results)} contacts in category '{category}':")
                    for contact_id in results:
                        display_contact(contacts_db, contact_id)
                else:
                    print(f"No contacts found in category '{category}'.")
                    
            elif search_choice == '3':
                phone = input("Enter phone number to search: ").strip()
                contact_id, contact_data = find_contact_by_phone(contacts_db, phone)
                if contact_id:
                    display_contact(contacts_db, contact_id)
                else:
                    print("No contact found with that phone number.")
                    
            else:
                print("Invalid search option.")
                
        elif choice == '3':
            # List all contacts
            list_all_contacts(contacts_db)
            
        elif choice == '4':
            # Update contact
            contact_id = input("Enter contact ID to update: ").strip()
            if contact_id in contacts_db:
                print("Leave field blank to keep current value.")
                
                field_updates = {}
                
                # Get updated values
                first_name = input(f"First Name ({contacts_db[contact_id]['first_name']}): ").strip()
                if first_name:
                    field_updates['first_name'] = first_name
                    
                last_name = input(f"Last Name ({contacts_db[contact_id]['last_name']}): ").strip()
                if last_name:
                    field_updates['last_name'] = last_name
                    
                phone = input(f"Phone ({contacts_db[contact_id]['phone']}): ").strip()
                if phone:
                    field_updates['phone'] = phone
                    
                email = input(f"Email ({contacts_db[contact_id]['email']}): ").strip()
                if email:
                    field_updates['email'] = email
                
                # Address updates
                address_updates = {}
                current_addr = contacts_db[contact_id].get('address', {})
                
                street = input(f"Street ({current_addr.get('street', '')}): ").strip()
                if street:
                    address_updates['street'] = street
                    
                city = input(f"City ({current_addr.get('city', '')}): ").strip()
                if city:
                    address_updates['city'] = city
                    
                state = input(f"State ({current_addr.get('state', '')}): ").strip()
                if state:
                    address_updates['state'] = state.upper()
                    
                zip_code = input(f"ZIP Code ({current_addr.get('zip_code', '')}): ").strip()
                if zip_code:
                    address_updates['zip_code'] = zip_code
                
                if address_updates:
                    field_updates['address'] = address_updates
                
                category = input(f"Category ({contacts_db[contact_id]['category']}): ").strip()
                if category:
                    field_updates['category'] = category
                    
                notes = input(f"Notes ({contacts_db[contact_id]['notes']}): ").strip()
                if notes:
                    field_updates['notes'] = notes
                
                if field_updates:
                    if update_contact(contacts_db, contact_id, field_updates):
                        print("Contact updated successfully.")
                else:
                    print("No changes made.")
            else:
                print("Contact ID not found.")
                
        elif choice == '5':
            # Delete contact
            contact_id = input("Enter contact ID to delete: ").strip()
            delete_contact(contacts_db, contact_id)
            
        elif choice == '6':
            # Merge contacts
            contact_id1 = input("Enter first contact ID to merge: ").strip()
            contact_id2 = input("Enter second contact ID to merge: ").strip()
            merge_contacts(contacts_db, contact_id1, contact_id2)
            
        elif choice == '7':
            # Generate statistics
            stats = generate_contact_statistics(contacts_db)
            print("\n--- Contact Statistics ---")
            print(f"Total contacts: {stats['total_contacts']}")
            print(f"Contacts by category: {stats['contacts_by_category']}")
            print(f"Contacts by state: {stats['contacts_by_state']}")
            print(f"Average contacts per category: {stats['average_contacts_per_category']:.2f}")
            print(f"Most common area code: {stats['most_common_area_code']}")
            print(f"Contacts without email: {stats['contacts_without_email']}")
            
        elif choice == '8':
            # Find duplicates
            duplicates = find_duplicate_contacts(contacts_db)
            print("\n--- Duplicate Contacts ---")
            
            has_duplicates = False
            
            if duplicates['phone_duplicates']:
                has_duplicates = True
                print("Phone duplicates:")
                for dup_list in duplicates['phone_duplicates']:
                    print(f"  {', '.join(dup_list)}")
                    
            if duplicates['email_duplicates']:
                has_duplicates = True
                print("Email duplicates:")
                for dup_list in duplicates['email_duplicates']:
                    print(f"  {', '.join(dup_list)}")
                    
            if duplicates['name_duplicates']:
                has_duplicates = True
                print("Name duplicates:")
                for dup_list in duplicates['name_duplicates']:
                    print(f"  {', '.join(dup_list)}")
            
            if not has_duplicates:
                print("No duplicates found.")
                
        elif choice == '9':
            # Export by category
            category = input("Enter category to export: ").strip()
            export_data = export_contacts_by_category(contacts_db, category)
            print(export_data)
            
            # Option to save to file
            save_file = input("Save to file? (y/n): ").strip().lower()
            if save_file == 'y':
                filename = input("Enter filename: ").strip()
                try:
                    with open(filename, 'w') as f:
                        f.write(export_data)
                    print(f"Data exported to {filename}")
                except IOError:
                    print("Error writing to file.")
                    
        elif choice == '10':
            # Save to file
            filename = input("Enter filename to save: ").strip()
            if filename:
                save_contacts_to_file(contacts_db, filename)
                
        elif choice == '11':
            # Load from file
            filename = input("Enter filename to load: ").strip()
            if filename:
                contacts_db = load_contacts_from_file(filename)
                
        elif choice == '12':
            # Exit
            save = input("Save before exiting? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Enter filename: ").strip()
                if filename:
                    save_contacts_to_file(contacts_db, filename)
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

def run_contact_manager():
    """
    Main function to run the contact management system.
    Initialize empty database and start the menu loop.
    """
    global contacts_db
    contacts_db = {}
    print("Welcome to the Contact Management System!")
    main_menu()

# Run the contact manager if this file is executed directly
if __name__ == "__main__":
    run_contact_manager()