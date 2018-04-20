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
        myfile = 'currency' + str(day_of_month) + '.json'
        my_file = Path(myfile)
        if my_file.is_file():
            return 1
        else:
            return 0

    def get_json(self):
        if self.is_json_locally()==0:
            self.json = json.load(urlopen(
                'https://openexchangerates.org/api/latest.json?app_id=eb234aa07f334a5aa05955f7a35f45d0'))
            print("nu este")
        else:
            print("ie")

    def copy_json_locally(self):
        file_name = 'currency' + str(datetime.datetime.today().day) + '.json'
        with open(file_name, 'w') as file:
            json.dump(self.json, file, ensure_ascii=False)


json1 = Json()
json1.get_json()
if not json1.is_json_locally():
    json1.copy_json_locally()