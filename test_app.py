import streamlit as st
import pytest
from unittest.mock import patch

# Import your Streamlit app
from app import main

def test_home_page(mocker):
    # Mock the Streamlit functions
    mock_write = mocker.patch("streamlit.write")

    # Run the Streamlit app
    main()

    # Check if the title is displayed correctly
    mock_write.assert_called_once_with("Hello World!")