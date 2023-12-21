import json
from SuricataEvent import SuricataEvent


def generate_events(path: str) -> list:
    with open(path, 'r') as eve:
        events_data = json.loads(eve)
        events = events_data['events']
    
    Suricata_events = []
    for event in events:
        Suricata_events.append(SuricataEvent(event['timestamp'], event['event_type'], event['src_ip'], event['dest_ip'], event['src_port'], event['dest_port'], event['proto'], event['flow_id']))

