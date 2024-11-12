# Streamlit quick start. 

 I'll structure it to cover all essential aspects.



```python
# streamlit_components_tutorial.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time
import plotly.express as px

def main():
    st.title("Streamlit UI Components Tutorial")
    
    # Sidebar Navigation
    section = st.sidebar.radio(
        "Choose a section",
        ["Basic Components", "Layout", "Input Widgets", "Charts & Media", "Advanced Components"]
    )

    if section == "Basic Components":
        show_basic_components()
    elif section == "Layout":
        show_layout_options()
    elif section == "Input Widgets":
        show_input_widgets()
    elif section == "Charts & Media":
        show_charts_and_media()
    else:
        show_advanced_components()

def show_basic_components():
    st.header("Basic Text Components")
    
    # Title and Headers
    st.subheader("1. Text Elements")
    st.write("Basic text using st.write()")
    st.text("Fixed width text using st.text()")
    st.markdown("**Markdown** formatting is *supported*")
    st.latex(r"E = mc^2")
    st.code("print('Hello, World!')", language='python')
    
    # Status Elements
    st.subheader("2. Status Elements")
    st.success("Success message")
    st.info("Info message")
    st.warning("Warning message")
    st.error("Error message")
    
    # Progress and Spinners
    st.subheader("3. Progress Indicators")
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
    
    with st.spinner("Loading..."):
        pass  # Simulating work
    
def show_layout_options():
    st.header("Layout Options")
    
    # Columns
    st.subheader("1. Columns")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Column 1")
        st.button("Button 1")
    with col2:
        st.write("Column 2")
        st.button("Button 2")
    with col3:
        st.write("Column 3")
        st.button("Button 3")
    
    # Containers
    st.subheader("2. Containers")
    with st.container():
        st.write("This is inside a container")
        st.button("Container Button")
    
    # Expanders
    st.subheader("3. Expanders")
    with st.expander("Click to expand"):
        st.write("Hidden content revealed!")
        st.image("https://placehold.co/600x400")
    
    # Tabs
    st.subheader("4. Tabs")
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("Content for tab 1")
    with tab2:
        st.write("Content for tab 2")

def show_input_widgets():
    st.header("Input Widgets")
    
    # Text Inputs
    st.subheader("1. Text Inputs")
    text_input = st.text_input("Enter some text")
    text_area = st.text_area("Multiline text")
    
    # Numeric Inputs
    st.subheader("2. Numeric Inputs")
    number = st.number_input("Enter a number", min_value=0, max_value=100)
    slider = st.slider("Select a range", 0, 100, (25, 75))
    
    # Selection Widgets
    st.subheader("3. Selection Widgets")
    option = st.selectbox(
        "Choose an option",
        ["Option 1", "Option 2", "Option 3"]
    )
    
    options = st.multiselect(
        "Select multiple options",
        ["Choice 1", "Choice 2", "Choice 3", "Choice 4"]
    )
    
    # Date and Time
    st.subheader("4. Date and Time")
    date = st.date_input("Select a date")
    time_input = st.time_input("Set a time")
    
    # File Uploader
    st.subheader("5. File Uploader")
    uploaded_file = st.file_uploader("Choose a file")
    
    # Forms
    st.subheader("6. Forms")
    with st.form("my_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        submit = st.form_submit_button("Submit")
        if submit:
            st.write(f"Submitted: {name}, {age}")

def show_charts_and_media():
    st.header("Charts and Media")
    
    # Sample data for charts
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # Line Chart
    st.subheader("1. Line Chart")
    st.line_chart(chart_data)
    
    # Area Chart
    st.subheader("2. Area Chart")
    st.area_chart(chart_data)
    
    # Bar Chart
    st.subheader("3. Bar Chart")
    st.bar_chart(chart_data)
    
    # Plotly Chart
    st.subheader("4. Plotly Chart")
    fig = px.scatter(chart_data, x='A', y='B', size='C')
    st.plotly_chart(fig)
    
    # Display Images
    st.subheader("5. Images")
    st.image("https://placehold.co/600x400", caption="Sample Image")
    
    # Display Video
    st.subheader("6. Video")
    st.video("https://placehold.co/600x400")

def show_advanced_components():
    st.header("Advanced Components")
    
    # Cache demonstration
    @st.cache_data
    def expensive_computation(a, b):
        return a + b
    
    # Session State
    st.subheader("1. Session State")
    if 'count' not in st.session_state:
        st.session_state.count = 0
    
    if st.button("Increment"):
        st.session_state.count += 1
    
    st.write("Count:", st.session_state.count)
    
    # Cached Function
    st.subheader("2. Cached Computation")
    result = expensive_computation(10, 20)
    st.write("Cached Result:", result)
    
    # Custom HTML/CSS
    st.subheader("3. Custom HTML/CSS")
    st.markdown("""
        <style>
        .custom-text {
            color: red;
            font-size: 20px;
        }
        </style>
        <p class='custom-text'>Styled text using HTML and CSS!</p>
    """, unsafe_allow_html=True)
    
    # Balloons
    st.subheader("4. Fun Elements")
    if st.button("Celebrate"):
        st.balloons()

if __name__ == "__main__":
    main()

```

Let me walk you through this tutorial step by step:

1. **Setting Up**
First, install the required packages:
```bash
pip install streamlit pandas numpy plotly
```

2. **Basic Components**
The tutorial starts with fundamental components:
- Text elements (write, text, markdown)
- Status messages (success, info, warning, error)
- Progress indicators

3. **Layout Options**
Learn how to structure your app using:
- Columns for side-by-side content
- Containers for grouping elements
- Expanders for collapsible sections
- Tabs for organized content

4. **Input Widgets**
Explore different ways to collect user input:
- Text inputs and text areas
- Numeric inputs and sliders
- Selection widgets (dropdown, multiselect)
- Date and time pickers
- File uploaders
- Forms

5. **Charts and Media**
Visualize data using:
- Built-in charts (line, area, bar)
- Plotly integration
- Image and video display

6. **Advanced Components**
Learn about:
- Session state management
- Caching for performance
- Custom styling with HTML/CSS
- Interactive elements

Let's try some practical examples:

1. **Create a Simple Form**
```python
with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Hello {name}, you are {age} years old!")
```

2. **Create a Dashboard Layout**
```python
col1, col2 = st.columns(2)
with col1:
    st.metric("Temperature", "70 °F", "1.2 °F")
with col2:
    st.metric("Humidity", "86%", "-4%")
```

3. **Add Interactive Charts**
```python
data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10)
})
st.line_chart(data)
```

Would you like me to:
1. Explain any specific component in more detail?
2. Show more examples of complex layouts?
3. Demonstrate how to combine multiple components?
4. Show how to create responsive designs?
5. Explain state management in more depth?

The code in the artifact provides a complete, runnable example of all these concepts. You can run it with:
```bash
streamlit run streamlit_components_tutorial.py
```


# Setup 

```bash
brew install conda 
```

```bash
# Create a new conda environment named 'streamlit' with Python 3.10
conda create -n streamlit python=3.10
```

# Activate the environment
```bash
conda activate streamlit
```

# Install all required packages
```bash
pip install streamlit pandas numpy plotly plotly-express
```

# Verify installations
```bash
python -c "import streamlit as st; import pandas as pd; import numpy as np; import plotly.express as px; print('All packages imported successfully!')"
```

# Create a new directory for your project
```bash
mkdir streamlit-tutorial
cd streamlit-tutorial
```

# Run the application (after saving the code from the previous artifact)
```bash
streamlit run streamlit_components_tutorial.py
```

If you encounter any issues:

1. Check environment activation:
```bash
# Should show 'streamlit' as active environment
conda env list
```

2. Check installed packages:
```bash
pip list
```

3. If you need to install additional packages later:
```bash
pip install package-name
```

4. If you want to export your environment:
```bash
pip freeze > requirements.txt
```

5. To install from requirements.txt in future:
```bash
pip install -r requirements.txt
```

Common troubleshooting:
1. If you get "command not found: streamlit", try:
```bash
python -m streamlit run streamlit_components_tutorial.py
```

2. If you need to reinstall packages:
```bash
pip uninstall package-name
pip install package-name
```

3. To check your Python path:
```bash
which python
```

