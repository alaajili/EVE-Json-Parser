import json
from SuricataEvent import SuricataEvent

def generate_events(path: str) -> list:
    """
    Reads a file containing Suricata event data in JSON format from the given 'path'.
    
    Parameters:
    - path (str): A string representing the file path containing Suricata event data.

    Returns:
    - list: A list of SuricataEvent objects parsed from the JSON file.
    """

    suricata_events = []
    with open(path, 'r') as eve:
        for line in eve:
            try:
                event_data = json.loads(line)
                suricata_events.append(SuricataEvent(event_data))
            except json.JSONDecodeError:
                continue
    return suricata_events


p = generate_events('eve.json')
print(p[1213].alert)
