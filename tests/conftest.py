import pytest
import os
import json

@pytest.fixture(autouse=True)
def clean_test_files():
    """Clean up test files before and after each test"""
    test_files = ['test_automations.json']
    
    # Clean before test
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)
    
    yield
    
    # Clean after test
    for file in test_files:
        if os.path.exists(file):
            os.remove(file) 