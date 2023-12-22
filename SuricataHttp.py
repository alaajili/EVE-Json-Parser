class SuricataHttp:
    def __init__(self, data):
        self.hostname = data.get('hostname', None)
        self.url = data.get('url', None)
        self.http_user_agent = data.get('http_user_agent', None)
        self.http_content_type = data.get('http_content_type', None)
        self.http_method = data.get('http_method', None)
        self.http_refer = data.get('http_refer', None)
        self.length = data.get('length', None)
        self.protocol = data.get('protocol', None)
        self.status = data.get('status', None)
        self.length = data.get('length', None)