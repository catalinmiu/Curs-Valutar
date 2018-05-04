import json
from urllib.request import urlopen
from pathlib import Path
import datetime
import os


class CurrencyJsonManager:

    @staticmethod
    def jsonExists(day_of_month=datetime.datetime.today().day):
        """Verify if Json is locally

            Args:
                day_of_month (Optional[Int]): If specified, the function will search
                a file with this pattern name 'currency[day_of_month].json'.
                Otherwise, the day will be the current day
        """
        file_name = 'JsonFiles/currency' + str(day_of_month) + '.json'
        file_name = Path(file_name)
        if file_name.is_file():
            return True

        return False

    @staticmethod
    def __getJsonFromAPI():
        return json.load(urlopen(
            'https://openexchangerates.org/api/latest.json?app_id=eb234aa07f334a5aa05955f7a35f45d0'))

    @staticmethod
    def storeJson():
        jsonContent = CurrencyJsonManager.__getJsonFromAPI()
        file_name = 'JsonFiles/currency' + str(datetime.datetime.today().day) + '.json'
        with open(file_name, 'w') as file:
            json.dump(jsonContent, file, ensure_ascii=False)

class CurrencyPrompt:
    def __init__(self):
        self.is_active = True

    @staticmethod
    def display(currency_name, day_of_month=datetime.datetime.today().day):
        file_name = 'JsonFiles/currency' + str(day_of_month) + '.json'
        with open(file_name, 'r') as f:
            curJson = json.load(f)
        print(curJson["rates"][currency_name])

    @staticmethod
    def refresh():
        CurrencyJsonManager.storeJson()

    def quit(self):
        self.is_active = False

    @staticmethod
    #get_history('USD')
    def get_history(currency_name):
        path = 'JsonFiles/'
        for file_name in os.listdir(path):
            file_name = 'JsonFiles/' + file_name
            with open(file_name, 'r') as f:
                datastore = json.load(f)
            file_date = datetime.datetime.fromtimestamp(datastore["timestamp"])
            print(str(file_date.strftime('%Y-%m-%d %H:%M:%S')) + " " + str(datastore["rates"][currency_name]))


class CursValutar():
    @staticmethod
    def main():
        if not CurrencyJsonManager.jsonExists():
            CurrencyJsonManager.storeJson()

        prompt = CurrencyPrompt()
        while prompt.is_active:
            command = input(">>sadffdsfsd")
            command = 'prompt.' + command
            try:
                eval(command)
            except:
                print("This is not a valid Command")

if __name__ == "__main__":
    app = CursValutar()
    app.main()