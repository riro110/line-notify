
import json
from dataclasses import dataclass

import requests


@dataclass
class LineNotify:
    token: str

    def __post_init__(self):
        self.header_base: dict = {
            "Authorization": f"Bearer {self.token}"
        }

    def notify(self, message: str, **other_params):
        url = 'https://notify-api.line.me/api/notify'

        headers = dict(self.header_base)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        payload = {'message': message}
        payload.update(other_params)

        res = requests.post(url, headers=headers, data=payload)
        if res.status_code != 200:
            raise Exception(f'HTTP Error {res.status_code}')

        return json.loads(res.text)
