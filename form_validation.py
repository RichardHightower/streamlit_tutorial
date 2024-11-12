import streamlit as st
from datetime import datetime, date, timedelta
import re


def create_sidebar_markdown(form_data):
    """Create a markdown summary of form data for the sidebar."""
    st.sidebar.markdown("---")
    st.sidebar.title("✨ Submission Summary")

    # Personal Details Section
    st.sidebar.header(f"👤 {form_data['first_name']} {form_data['last_name']}")

    # Contact Information
    st.sidebar.subheader("📞 Contact Details")
    st.sidebar.markdown(f"""
    - 📧 {form_data['email']}
    - ☎️ {form_data['phone']}
    """)

    # Personal Information
    st.sidebar.subheader("ℹ️ Personal Info")
    st.sidebar.markdown(f"""
    - 🎂 Age: {form_data['age']}
    - 📅 Birth Date: {form_data['birth_date'].strftime('%Y-%m-%d')}
    """)

    # Schedule Information
    st.sidebar.subheader("📅 Schedule")
    st.sidebar.markdown(f"""
    | Date Type | Value |
    |-----------|-------|
    | Start | {form_data['start_date'].strftime('%Y-%m-%d')} |
    | End | {form_data['end_date'].strftime('%Y-%m-%d')} |
    """)

    # Submission Details
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"*Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    # Add Clear Form Button to Sidebar
    if st.sidebar.button("🔄 Clear Form"):
        return True
    return False


def validate_name(name, field_name="Name"):
    """Validate name contains only letters, spaces, and hyphens."""
    if not name:
        return False, f"{field_name} is required"
    if not re.match(r'^[A-Za-z\s-]+$', name):
        return False, f"{field_name} should only contain letters, spaces, and hyphens"
    if len(name) < 2:
        return False, f"{field_name} should be at least 2 characters long"
    return True, ""


def validate_email(email):
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Please enter a valid email address"
    return True, ""


def validate_phone(phone):
    """Validate phone number format."""
    pattern = r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$'
    if not re.match(pattern, phone):
        return False, "Please enter a valid phone number"
    return True, ""


def validate_age(age):
    """Validate age is between 0 and 120."""
    try:
        age = int(age)
        if age < 0 or age > 120:
            return False, "Age must be between 0 and 120"
        return True, ""
    except ValueError:
        return False, "Please enter a valid number"


def validate_date(input_date, earliest_date=date(1990, 1, 1)):
    """Validate date is after 1989 and not more than 5 years in future."""
    max_future_date = date.today() + timedelta(days=5 * 365)
    if input_date < earliest_date:
        return False, f"Date must be after {earliest_date.strftime('%Y-%m-%d')}"
    elif input_date > max_future_date:
        return False, f"Date cannot be more than 5 years in the future"
    return True, ""


def main():
    st.title("✨ Enhanced Form Validation")

    # Initialize session state
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'age': '',
            'birth_date': date.today(),
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=1),
            'submitted': False
        }

    # Display initial sidebar content
    if not st.session_state.form_data['submitted']:
        st.sidebar.title("📝 Form Status")
        st.sidebar.info("Please fill out the form to see the summary.")

    # Main form
    with st.form("enhanced_validation"):
        st.header("👤 Personal Information")

        # Name fields in columns
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input(
                "First Name",
                value=st.session_state.form_data['first_name']
            )
            if first_name:
                is_valid, message = validate_name(first_name, "First name")
                if not is_valid:
                    st.error(message)
                else:
                    st.success("Valid first name!")

        with col2:
            last_name = st.text_input(
                "Last Name",
                value=st.session_state.form_data['last_name']
            )
            if last_name:
                is_valid, message = validate_name(last_name, "Last name")
                if not is_valid:
                    st.error(message)
                else:
                    st.success("Valid last name!")

        # Contact Information
        st.header("📞 Contact Information")
        email = st.text_input(
            "Email",
            value=st.session_state.form_data['email']
        )
        if email:
            is_valid, message = validate_email(email)
            if not is_valid:
                st.error(message)
            else:
                st.success("Valid email format!")

        phone = st.text_input(
            "Phone",
            value=st.session_state.form_data['phone'],
            help="Format: (123) 456-7890 or 123-456-7890"
        )
        if phone:
            is_valid, message = validate_phone(phone)
            if not is_valid:
                st.error(message)
            else:
                st.success("Valid phone number!")

        # Age and Birth Date
        st.header("📅 Personal Details")
        col3, col4 = st.columns(2)
        with col3:
            age = st.number_input(
                "Age",
                min_value=0,
                max_value=120,
                value=0 if not st.session_state.form_data['age'] else \
                    int(st.session_state.form_data['age'])
            )
            if age:
                is_valid, message = validate_age(age)
                if not is_valid:
                    st.error(message)
                else:
                    st.success("Valid age!")

        with col4:
            birth_date = st.date_input(
                "Birth Date",
                value=st.session_state.form_data['birth_date']
            )
            if birth_date:
                is_valid, message = validate_date(birth_date)
                if not is_valid:
                    st.error(message)
                else:
                    st.success("Valid birth date!")

        # Schedule Information
        st.header("📅 Schedule")
        col5, col6 = st.columns(2)
        with col5:
            start_date = st.date_input(
                "Start Date",
                value=st.session_state.form_data['start_date']
            )
        with col6:
            end_date = st.date_input(
                "End Date",
                value=st.session_state.form_data['end_date']
            )

        if start_date and end_date and start_date >= end_date:
            st.error("Start date must be before end date")

        submitted = st.form_submit_button("Submit Form")
        if submitted:
            # Validate all fields
            validations = [
                validate_name(first_name, "First name"),
                validate_name(last_name, "Last name"),
                validate_email(email),
                validate_phone(phone),
                validate_age(age),
                validate_date(birth_date),
                (start_date < end_date, "Start date must be before end date")
            ]

            # Check if all validations pass
            if all(v[0] for v in validations):
                st.success("Form submitted successfully!")
                # Update session state
                st.session_state.form_data.update({
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone': phone,
                    'age': age,
                    'birth_date': birth_date,
                    'start_date': start_date,
                    'end_date': end_date,
                    'submitted': True
                })
                st.rerun()
            else:
                # Show all validation errors
                for valid, message in validations:
                    if not valid:
                        st.error(message)

    # Display summary in sidebar after successful submission
    if st.session_state.form_data['submitted']:
        if create_sidebar_markdown(st.session_state.form_data):
            # Clear form if button clicked
            for key in st.session_state.form_data:
                if key in ['start_date', 'end_date', 'birth_date']:
                    st.session_state.form_data[key] = date.today()
                elif key == 'submitted':
                    st.session_state.form_data[key] = False
                else:
                    st.session_state.form_data[key] = ''
            st.rerun()


if __name__ == "__main__":
    main()