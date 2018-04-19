import json
from urllib.request import urlopen

class Json:
    def __init__(self, json1):
        self.json1 = json1

    def write_currency_values_to_file(self):
        with open("currency.txt", "w") as file:
            for i in range(0,10):
                file.write(self.json1['base'][i])
            file.close()



class Curs:
    def __init__(self):
        pass

    def get_data(self):
        data = json.load(urlopen(
            'https://openexchangerates.org/api/latest.json?app_id=eb234aa07f334a5aa05955f7a35f45d0'))
        print(data)
        #json1.write_currency_values_to_file()

curs = Curs()
curs.get_data()