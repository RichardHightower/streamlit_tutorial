import streamlit as st
from datetime import datetime, date, timedelta
import re


def validate_name(name, field_name):
    if not name:
        return False, f"{field_name} is required"
    if not re.match(r"^[a-zA-Z'\s\-]{2,50}$", name):
        return False, f"{field_name} must contain only letters, spaces, hyphens, or apostrophes (2-50 characters)"
    return True, ""


def validate_email(email):
    if not email:
        return False, "Email is required"
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False, "Invalid email format"
    return True, ""


def validate_phone(phone):
    if not phone:
        return False, "Phone number is required"
    clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
    if not re.match(r'^[0-9]{10}$', clean_phone):
        return False, "Phone must be 10 digits"
    return True, ""


def validate_age(age):
    if age <= 0:
        return False, "Age must be greater than 0"
    if age > 120:
        return False, "Age must be less than 120"
    return True, ""


def validate_date(check_date):
    if not check_date:
        return False, "Date is required"
    if check_date > date.today():
        return False, "Date cannot be in the future"
    return True, ""


def get_validation_status():
    """Get detailed validation status for all fields"""
    validation_messages = []

    # Check each field and collect validation messages
    if not st.session_state.get('first_name_valid', False):
        if st.session_state.get('first_name', ''):
            is_valid, message = validate_name(st.session_state.first_name, "First name")
            if not is_valid:
                validation_messages.append(message)
        else:
            validation_messages.append("First name is required")

    if not st.session_state.get('last_name_valid', False):
        if st.session_state.get('last_name', ''):
            is_valid, message = validate_name(st.session_state.last_name, "Last name")
            if not is_valid:
                validation_messages.append(message)
        else:
            validation_messages.append("Last name is required")

    if not st.session_state.get('email_valid', False):
        if st.session_state.get('email', ''):
            is_valid, message = validate_email(st.session_state.email)
            if not is_valid:
                validation_messages.append(message)
        else:
            validation_messages.append("Email is required")

    if not st.session_state.get('phone_valid', False):
        if st.session_state.get('phone', ''):
            is_valid, message = validate_phone(st.session_state.phone)
            if not is_valid:
                validation_messages.append(message)
        else:
            validation_messages.append("Phone number is required")

    if not st.session_state.get('age_valid', False):
        if st.session_state.get('age', 0) > 0:
            is_valid, message = validate_age(st.session_state.age)
            if not is_valid:
                validation_messages.append(message)
        else:
            validation_messages.append("Age is required")

    if not st.session_state.get('birth_date_valid', False):
        if st.session_state.get('birth_date'):
            is_valid, message = validate_date(st.session_state.birth_date)
            if not is_valid:
                validation_messages.append(message)
        else:
            validation_messages.append("Birth date is required")

    # Check date range
    start_date = st.session_state.get('start_date')
    end_date = st.session_state.get('end_date')
    if start_date and end_date and start_date >= end_date:
        validation_messages.append("Start date must be before end date")

    return validation_messages


def update_sidebar_table():
    st.sidebar.title("📝 Form Data")

    # Get current values from session state
    current_data = {
        'First Name': st.session_state.get('first_name', ''),
        'Last Name': st.session_state.get('last_name', ''),
        'Email': st.session_state.get('email', ''),
        'Phone': st.session_state.get('phone', ''),
        'Age': st.session_state.get('age', 0),
        'Birth Date': st.session_state.get('birth_date', date.today()),
        'Start Date': st.session_state.get('start_date', date.today()),
        'End Date': st.session_state.get('end_date', date.today())
    }

    # Create markdown table
    table_header = "| Field | Value | Status |\n|--------|--------|--------|\n"
    table_rows = ""

    for field, value in current_data.items():
        # Format value based on type
        if isinstance(value, date):
            formatted_value = value.strftime('%Y-%m-%d')
        elif isinstance(value, (int, float)):
            formatted_value = str(value) if value != 0 else ''
        else:
            formatted_value = str(value)

        # Determine validation status
        field_key = field.lower().replace(' ', '_')
        if field in ['Start Date', 'End Date']:
            start_date = st.session_state.get('start_date')
            end_date = st.session_state.get('end_date')
            is_valid = start_date and end_date and start_date < end_date
        else:
            is_valid = st.session_state.get(f'{field_key}_valid', False)

        # Add status emoji
        status = "✅" if is_valid and formatted_value else "❌" if formatted_value else "⏳"

        table_rows += f"| {field} | {formatted_value} | {status} |\n"

    st.sidebar.markdown(table_header + table_rows)

    if st.session_state.get('form_submitted', False):
        st.sidebar.success("Form submitted successfully!")

    if st.sidebar.button("Clear Form"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()


def main():
    st.set_page_config(
        page_title="Real-time Form Validation",
        page_icon="✨",
        layout="wide"
    )

    st.title("✨ Real-time Form Validation")

    # Initialize session state
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False

    # Initialize validation summary
    if 'validation_messages' not in st.session_state:
        st.session_state.validation_messages = []

    # Create columns for the form and validation messages
    form_col, validation_col = st.columns([2, 1])

    with form_col:
        # Personal Information
        st.header("👤 Personal Information")

        # First Name (with real-time validation)
        first_name = st.text_input("First Name", key="first_name")
        if first_name:  # Only validate if there's input
            is_valid, message = validate_name(first_name, "First name")
            st.session_state.first_name_valid = is_valid
            if not is_valid:
                st.error(message)
            else:
                st.success("Valid first name!")
        else:
            st.session_state.first_name_valid = False

        # Last Name
        last_name = st.text_input("Last Name", key="last_name")
        if last_name:
            is_valid, message = validate_name(last_name, "Last name")
            st.session_state.last_name_valid = is_valid
            if not is_valid:
                st.error(message)
            else:
                st.success("Valid last name!")
        else:
            st.session_state.last_name_valid = False

        # Contact Information
        st.header("📞 Contact Information")

        # Email
        email = st.text_input("Email", key="email")
        if email:
            is_valid, message = validate_email(email)
            st.session_state.email_valid = is_valid
            if not is_valid:
                st.error(message)
            else:
                st.success("Valid email!")
        else:
            st.session_state.email_valid = False

        # Phone
        phone = st.text_input("Phone", help="Format: (123) 456-7890 or 123-456-7890", key="phone")
        if phone:
            is_valid, message = validate_phone(phone)
            st.session_state.phone_valid = is_valid
            if not is_valid:
                st.error(message)
            else:
                st.success("Valid phone number!")
        else:
            st.session_state.phone_valid = False

        # Personal Details
        st.header("📅 Personal Details")
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=0, max_value=120, key="age")
            if age > 0:
                is_valid, message = validate_age(age)
                st.session_state.age_valid = is_valid
                if not is_valid:
                    st.error(message)
                else:
                    st.success("Valid age!")
            else:
                st.session_state.age_valid = False

        with col2:
            birth_date = st.date_input("Birth Date", key="birth_date")
            if birth_date:
                is_valid, message = validate_date(birth_date)
                st.session_state.birth_date_valid = is_valid
                if not is_valid:
                    st.error(message)
                else:
                    st.success("Valid birth date!")
            else:
                st.session_state.birth_date_valid = False

        # Schedule
        st.header("📅 Schedule")
        col3, col4 = st.columns(2)

        with col3:
            start_date = st.date_input("Start Date", key="start_date")
        with col4:
            end_date = st.date_input("End Date", key="end_date")

        if start_date and end_date:
            if start_date >= end_date:
                st.error("Start date must be before end date")
                st.session_state.start_date_valid = False
                st.session_state.end_date_valid = False
            else:
                st.success("Valid date range!")
                st.session_state.start_date_valid = True
                st.session_state.end_date_valid = True

        # Submit button
        if st.button("Submit"):
            # Get validation messages
            validation_messages = get_validation_status()

            if not validation_messages:
                st.success("Form submitted successfully!")
                st.session_state.form_submitted = True
            else:
                st.error("Please fix the following validation errors:")
                for message in validation_messages:
                    st.error(f"• {message}")

    # Update sidebar with current form data
    update_sidebar_table()

    # Display validation summary in the validation column
    with validation_col:
        st.header("Validation Summary")
        all_valid = not get_validation_status()
        if all_valid:
            st.success("All fields are valid! ✨")
        else:
            messages = get_validation_status()
            st.error("Fields needing attention:")
            for message in messages:
                st.warning(f"• {message}")


if __name__ == "__main__":
    main()