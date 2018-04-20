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
        self.is_active = True

    def show_currency(self, currency_name, day_of_month=datetime.datetime.today().day):
        file_name = file_name = 'currency' + str(day_of_month) + '.json'
        if file_name:
            with open(file_name, 'r') as f:
                datastore = json.load(f)

        print(datastore["rates"][currency_name])

json1 = Json()
json1.get_json()
if not json1.is_json_locally():
    json1.copy_json_locally()

prompt = CurrencyPrompt()

while prompt.is_active:
    command = input(">>")
    try:
        prompt.show_currency(command)
    except KeyError:
        if command=="quit":
            prompt.is_active = False
            break
        print("This is not a valid Command")
