import json
from urllib.request import urlopen
from pathlib import Path
import datetime

class Json:
    def __init__(self):
        self.json = None

    @staticmethod
    def is_json_locally(day_of_month=datetime.datetime.today().day):
        """"Verify if Json is locally

            Args:
                day_of_month (Optional[Int]): If specified, the function will search
                a file with this pattern name 'currency[day_of_month].json'.
                Otherwise, the day will be the current day
        """
        file_name = 'currency' + str(day_of_month) + '.json'
        file_name = Path(file_name)
        if file_name.is_file():
            return True
        else:
            return False

    def get_json(self):
        if not self.is_json_locally():
            self.json = json.load(urlopen(
                'https://openexchangerates.org/api/latest.json?app_id=eb234aa07f334a5aa05955f7a35f45d0'))

    def copy_json_locally(self):
        file_name = 'currency' + str(datetime.datetime.today().day) + '.json'
        with open(file_name, 'w') as file:
            json.dump(self.json, file, ensure_ascii=False)


class CurrencyPrompt:
    def __init__(self):
        pass


json1 = Json()
json1.get_json()
if not json1.is_json_locally():
    json1.copy_json_locally()