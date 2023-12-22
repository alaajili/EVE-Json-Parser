class SuricataFlow:
    def __init__(self, data):
        self.pkts_toserver = data.get('pkts_toserver', None)
        self.pkts_toclient = data.get('pkts_toclient', None)
        self.bytes_toserver = data.get('bytes_toserver', None)
        self.bytes_toclient = data.get('bytes_toclient', None)
        if 'bypassed' in data:
            self.bypassed = ByPassed(data['bypassed'])
        self.start = data.get('start', None)
        self.end = data.get('end', None)
        self.age = data.get('age', None)
        self.bypass = data.get('bypass', None)
        self.reason = data.get('reason', None)
        self.alerted = data.get('alerted', None)

class ByPassed:
    def __init__(self, data):
        self.pkts_toserver = data.get('pkts_toserver', None)
        self.pkts_toclient = data.get('pkts_toclient', None)
        self.bytes_toserver = data.get('bytes_toserver', None)
        self.bytes_toclient = data.get('bytes_toclient', None)
        