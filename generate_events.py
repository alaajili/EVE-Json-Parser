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
            event_data = json.loads(line)
            try:
                # Check if all necessary keys exist before creating the SuricataEvent object
                if all(key in event_data for key in ['timestamp', 'event_type', 'src_ip', 'dest_ip', 'src_port', 'dest_port', 'proto', 'flow_id']):
                    event = SuricataEvent(
                        event_data['timestamp'],
                        event_data['event_type'],
                        event_data['src_ip'],
                        event_data['dest_ip'],
                        event_data['src_port'],
                        event_data['dest_port'],
                        event_data['proto'],
                        event_data['flow_id']
                    )

                    if event.event_type == 'alert':
                        event.alert = event_data['alert']
                    elif event.event_type == 'http':
                        event.http = event_data['http']
                    elif event.event_type == 'anomaly':
                        event.anomaly = event_data['anomaly']
                    elif event.event_type == 'flow':
                        event.flow = event_data['flow']
                    suricata_events.append(event)
                else:
                    # If any of the keys are missing, skip this entry
                    continue
            except json.JSONDecodeError:
                continue
    return suricata_events


