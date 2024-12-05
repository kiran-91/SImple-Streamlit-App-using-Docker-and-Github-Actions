import streamlit as st
import pytest
from streamlit.testing import StreamlitTest

# Import your Streamlit app
from app import main

# Define a test case class
class TestStreamlitApp(StreamlitTest):
    
    def test_home_page(self):
        # Run the Streamlit app
        self.run_app(main)

        # Check if the title is displayed correctly
        assert self.get_text("Hello World!") is not None

if __name__ == "__main__":
    pytest.main()