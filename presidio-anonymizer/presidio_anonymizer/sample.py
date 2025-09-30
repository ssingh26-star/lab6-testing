from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text=None, start=None, end=None):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Use provided parameters or get from input
    if text is None:
        text = input("text: ")
    if start is None:
        start = int(input("start: "))
    if end is None:
        end = int(input("end: "))

    # Invoke the anonymize function with the text,
    # analyze results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return result

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

if __name__ == "__main__":
    # For interactive use, get input from user
    result = sample_run_anonymizer()
    print("text: ", result.text)
    print("items:")
    
    print(result.items)
