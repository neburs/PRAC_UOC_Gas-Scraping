import requests


class WebService:
    @staticmethod
    def download_html(url: str, headers: dict, params: tuple, data: dict) -> str:

        response = requests.post(url, headers=headers, params=params, data=data)

        if response.status_code != 200:
            print("Invalid url " + url)
            return ''

        content = response.text

        return content
