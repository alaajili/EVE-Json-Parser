class SuricataAnomaly:
    def __init__(self, data):
        self.app_proto = data.get('app_proto', None)
        self.event = data.get('event', None)
        self.layer = data.get('layer', None)
        self.type = data.get('type', None)
