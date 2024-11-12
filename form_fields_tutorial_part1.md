I'll break down the form validation tutorial into clear, manageable steps.





# Streamlit Form Validation Tutorial - Step by Step Guide

## Step 1: Project Setup

First, create your project environment and install required packages:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install streamlit
```

Create a new file named `form_validation.py`.

## Step 2: Import Required Libraries

```python
import streamlit as st
import re
from datetime import datetime, date, timedelta
```

## Step 3: Create Validation Functions

### 3.1 Name Validation
```python
def validate_name(name, field_name="Name"):
    if not name:
        return False, f"{field_name} is required"
    if not re.match(r'^[A-Za-z\s-]+$', name):
        return False, f"{field_name} should only contain letters, spaces, and hyphens"
    if len(name) < 2:
        return False, f"{field_name} should be at least 2 characters long"
    return True, ""
```

### 3.2 Email Validation
```python
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Please enter a valid email address"
    return True, ""
```

### 3.3 Phone Validation
```python
def validate_phone(phone):
    pattern = r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$'
    if not re.match(pattern, phone):
        return False, "Please enter a valid phone number"
    return True, ""
```

### 3.4 Date Validation
```python
def validate_date(input_date, earliest_date=date(1990, 1, 1)):
    max_future_date = date.today() + timedelta(days=5*365)
    if input_date < earliest_date:
        return False, f"Date must be after {earliest_date.strftime('%Y-%m-%d')}"
    elif input_date > max_future_date:
        return False, f"Date cannot be more than 5 years in the future"
    return True, ""
```

## Step 4: Create Summary Function

```python
def create_summary_markdown(form_data):
    markdown = f"""
    # {form_data['first_name']} {form_data['last_name']}

    ## Personal Information

    | Field | Value |
    |-------|-------|
    | First Name | {form_data['first_name']} |
    | Last Name | {form_data['last_name']} |
    | Email | {form_data['email']} |
    | Phone | {form_data['phone']} |
    | Age | {form_data['age']} |
    | Birth Date | {form_data['birth_date'].strftime('%Y-%m-%d')} |
    """
    return markdown
```

## Step 5: Initialize Session State

In your main function, add:
```python
def main():
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
```

## Step 6: Create Form Layout

### 6.1 Basic Form Structure
```python
with st.form("enhanced_validation"):
    st.header("Personal Information")
```

### 6.2 Add Name Fields with Columns
```python
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
```

### 6.3 Add Contact Information
```python
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
```

## Step 7: Implement Form Submission

```python
    submitted = st.form_submit_button("Submit Form")
    if submitted:
        validations = [
            validate_name(first_name, "First name"),
            validate_name(last_name, "Last name"),
            validate_email(email),
            validate_phone(phone),
            validate_age(age),
            validate_date(birth_date),
            (start_date < end_date, "Start date must be before end date")
        ]
        
        if all(v[0] for v in validations):
            st.success("Form submitted successfully!")
            st.session_state.form_data.update({
                'first_name': first_name,
                'last_name': last_name,
                # ... other fields ...
                'submitted': True
            })
```

## Step 8: Display Summary

```python
    if st.session_state.form_data['submitted']:
        st.markdown("---")
        st.header("Form Submission Summary")
        summary_markdown = create_summary_markdown(st.session_state.form_data)
        st.markdown(summary_markdown)
```

## Step 9: Add Clear Form Functionality

```python
        if st.button("Clear Form"):
            for key in st.session_state.form_data:
                if key in ['start_date', 'end_date', 'birth_date']:
                    st.session_state.form_data[key] = date.today()
                elif key == 'submitted':
                    st.session_state.form_data[key] = False
                else:
                    st.session_state.form_data[key] = ''
            st.rerun()
```

## Key Concepts Explained

1. **Real-time Validation**
   - Each field is validated as the user types
   - Immediate feedback through success/error messages
   - All validations are rechecked on submission

2. **Session State**
   - Persists form data between reruns
   - Maintains form state (submitted/not submitted)
   - Allows for form clearing and resetting

3. **Form Layout**
   - Uses columns for better space utilization
   - Groups related fields together
   - Clear visual hierarchy with headers

4. **Validation Patterns**
   - Regular expressions for format validation
   - Date range checks
   - Required field validation
   - Custom validation messages

5. **Summary Display**
   - Markdown formatting for clean presentation
   - Table layout for data organization
   - Timestamp for submission tracking

## Testing Your Form

1. Run the application:
```bash
streamlit run form_validation.py
```

2. Test validation by:
   - Entering invalid emails
   - Testing date ranges
   - Submitting incomplete forms
   - Checking real-time validation messages

3. Test form submission:
   - Submit with all valid data
   - Verify summary display
   - Test clear form functionality

## Common Issues and Solutions

1. **Date Validation Issues**
   - Ensure datetime imports are correct
   - Check timezone handling if needed
   - Verify date comparison logic

2. **State Management**
   - Use st.session_state for persistence
   - Clear state appropriately
   - Handle state initialization

3. **Form Submission**
   - Validate all fields before submission
   - Handle empty fields appropriately
   - Provide clear feedback

Next Steps:
1. Add more examples of validation patterns?
2. Show how to handle more complex form scenarios?
3. Demonstrate additional styling options?
4. Add more error handling examples?
5. Realtime for field validation as you type
