from win10toast import ToastNotifier
from datetime import datetime
import webbrowser
import json
import time

def notif(tittle, body):
    toaster = ToastNotifier()
    toaster.show_toast(tittle, body)

def open_in_browser(url):
    webbrowser.open(url)

def get_date():
    day = datetime.today().strftime('%A')
    hour = datetime.today().hour
    minute = datetime.today().minute
    time = '{}:{}'.format(hour, minute)

    return {"day": day, "time": time}

def read_json_file(filename):
    myFile = open(filename)
    data = json.load(myFile)
    date = get_date()

    for dayInstance in data:
        if dayInstance['dia'] == date['day']:
            for myClass in dayInstance['clases']:
                if myClass['start'] == date['time']:
                    open_in_browser(myClass['url'])
                    notif(myClass['nombre'], 'La clase empieza {}\nLa clase temina {}\nSuerte!'.format(myClass['start'], myClass['end']))
                    print(myClass['nombre'])
                    time.sleep(70)
                elif myClass['end'] == date['time']:
                    notif('Ha termidado la clase')
                    print("End")
                    time.sleep(70)

    myFile.close()

def main():
    read_json_file('schedule.json')


if __name__ == "__main__":
    print('Schedule manager\n[i] Active')
    while True:
        main()