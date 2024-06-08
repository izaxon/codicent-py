import requests

class Codicent:
    def __init__(self, token, signalr_host=None):
        self.token = token
        self.signalr_host = signalr_host
        self.base_url = "https://codicent.com/app"

    def init(self):
        # No-op, initialization is done in the constructor
        pass

    def upload(self, file):
        url = f"{self.base_url}/upload"
        files = {"file": file}
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(url, files=files, headers=headers)
        return response.json()["id"]

    def post_message(self, message, parent_id=None, type="info"):
        url = f"{self.base_url}/AddChatMessage"
        data = {"content": message, "type": type, "isNew": False }
        if parent_id:
            data["parentId"] = parent_id
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        return response.json()["id"]

    def get_messages(self, start=0, length=10, search="", after_timestamp=None, before_timestamp=None):
        url = f"{self.base_url}/GetChatMessages"
        params = {"start": start, "length": length, "search": search}
        if after_timestamp:
            params["afterTimestamp"] = after_timestamp.isoformat()
        if before_timestamp:
            params["beforeTimestamp"] = before_timestamp.isoformat()
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, params=params, headers=headers)
        return response.json()