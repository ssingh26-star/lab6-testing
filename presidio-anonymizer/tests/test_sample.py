import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer_basic_functionality():
    """Test the refactored sample_run_anonymizer function with known inputs."""
    # Test data - Bond example
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    # Verify the result structure and content
    assert result.text == "My name is BIP."
    assert len(result.items) == 1
    assert result.items[0].start == 11
    assert result.items[0].end == 14
    assert result.items[0].entity_type == 'PERSON'
    assert result.items[0].text == 'BIP'
    assert result.items[0].operator == 'replace'