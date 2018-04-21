import json
from urllib.request import urlopen
from pathlib import Path
import datetime


class Json:
    def __init__(self):
        self.json = None

    @staticmethod
    def exists(day_of_month=datetime.datetime.today().day):
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

    def __load(self):
        self.json = json.load(urlopen(
            'https://openexchangerates.org/api/latest.json?app_id=eb234aa07f334a5aa05955f7a35f45d0'))

    @classmethod
    def save(self, refresh=0):
        if self.exists() == 0 or refresh == 1:
            self.__load(self)
            file_name = 'JsonFiles/currency' + str(datetime.datetime.today().day) + '.json'
            with open(file_name, 'w') as file:
                json.dump(self.json, file, ensure_ascii=False)
            print("save")


class CurrencyPrompt:
    def __init__(self):
        self.is_active = True

    def display(self, currency_name, day_of_month=datetime.datetime.today().day):
        file_name = file_name = 'JsonFiles/currency' + str(day_of_month) + '.json'
        if file_name:
            with open(file_name, 'r') as f:
                datastore = json.load(f)
        print(datastore["rates"][currency_name])

    def quit(self):
        self.is_active = False

    def refresh(self):
        Json.save(1)

class CursValutar():
    @staticmethod
    def main():
        json1 = Json()
        json1.save()

        prompt = CurrencyPrompt()
        while prompt.is_active:
            command = input(">>")
            command = 'prompt.' + command
            try:
                eval(command)
            except:
                print("This is not a valid Command")

if __name__ == "__main__":
    app = CursValutar()
    app.main()