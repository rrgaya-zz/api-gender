import requests


class GenderDetector:

    def __init__(self) -> None:
        pass
    
    def run(self, name):
        url =  f"https://api.genderize.io/?name={name}"
        result = requests.get(url).json()
        return result['gender']