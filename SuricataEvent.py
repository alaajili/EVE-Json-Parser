class SuricataEvent:
    def __init__(self, timestamp, event_type, src_ip, dest_ip, src_port, dest_port, proto, flow_id) -> None:
        self.timestamp = timestamp
        self.event_type = event_type
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.src_port = src_port
        self.dest_port = dest_port
        self.proto = proto
        self.flow_id = flow_id

