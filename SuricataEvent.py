from SuricataFlow import SuricataFlow
from SuricataAlert import SuricataAlert
from SuricataHttp import SuricataHttp
from SuricataAnomaly import SuricataAnomaly

class SuricataEvent:
    def __init__(self, data) -> None:
        self.timestamp = data.get('timestamp', None)
        self.flow_id = data.get('flow_id', None)
        self.pcap_cnt = data.get('pcap_cnt', None)
        self.event_type = data.get('event_type', None)
        self.src_ip = data.get('src_ip', None)
        self.src_port = data.get('src_port', None)
        self.dest_ip = data.get('dest_ip', None)
        self.dest_port = data.get('dest_port', None)
        self.proto = data.get('proto', None)
        self.pkt_src = data.get('pkt_src', None)
        if 'flow' in data:
            self.flow = SuricataFlow(data['flow'])
        else:
            self.flow = None
        if 'alert' in data:
            self.alert = SuricataAlert(data['alert'])
        else:
            self.alert = None
        if 'http' in data:
            self.http = SuricataHttp(data['http'])
        else:
            self.http = None
        if 'anomaly' in data:
            self.anomaly = SuricataAnomaly(data['anomaly'])
        else:
            self.anomaly = None

        # you can add more attributes here if you want
