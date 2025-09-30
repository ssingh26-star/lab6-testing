import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # replace the following line with your test
    # Test data
    test_text = "My name is Bond."
    test_start = 11
    test_end = 15
    
    # Call the function with test parameters
    result = sample_run_anonymizer(text=test_text, start=test_start, end=test_end)
    
    # Verify the result structure and content
    assert result.text == "My name is BIP."
    assert len(result.items) == 1
    
    item = result.items[0]
    # Use dot notation to access attributes, not dictionary indexing
    assert item.start == 11
    assert item.end == 14  # "BIP" is 3 chars vs "Bond" which is 4
    assert item.entity_type == 'PERSON'
    assert item.text == 'BIP'
    assert item.operator == 'replace'