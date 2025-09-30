"""Sample module for demonstrating anonymization functionality."""

from presidio_anonymizer.entities import OperatorConfig, RecognizerResult
from presidio_anonymizer import AnonymizerEngine


def sample_run_anonymizer(text=None, start=None, end=None):
    """Run the anonymizer with optional parameters for testing.
    
    Args:
        text: Input text to anonymize
        start: Start index of entity to anonymize
        end: End index of entity to anonymize
        
    Returns:
        Anonymization result object
    """
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text,
    # analyze results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type="PERSON", start=start, end=end, score=0.8
            )
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return result


def main():
    """Main function for interactive use."""
    text = input("text: ")
    start = int(input("start: "))
    end = int(input("end: "))
    
    result = sample_run_anonymizer(text, start, end)
    print("text:", result.text)
    print("items:")
    print(result.items)


if __name__ == "__main__":
    # Test with the Bond example
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    print("text:", result.text)
    print("items:")
    print(result.items)

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

