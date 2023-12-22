class SuricataAlert:
    def __init__(self, data):
        self.action = data.get('action', None)
        self.gid = data.get('gid', None)
        self.signature_id = data.get('signature_id', None)
        self.rev = data.get('rev', None)
        self.signature = data.get('signature', None)
        self.category = data.get('category', None)
        self.severity = data.get('severity', None)
        if 'metadata' in data:
            self.metadata = Metadata(data['metadata'])


class Metadata:
    def __init__(self, data):
        self.affected_product = data.get('affected_product', None)
        self.attack_target = data.get('attack_target', None)
        self.created_at = data.get('created_at', None)
        self.deployment = data.get('deployment', None)
        self.former_category = data.get('former_category', None)
        self.malware_family = data.get('malware_family', None)
        self.performance_impact = data.get('performance_impact', None)
        self.signature_severity = data.get('signature_severity', None)
        self.updated_at = data.get('updated_at', None)