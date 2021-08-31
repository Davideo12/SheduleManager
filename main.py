from win10toast import ToastNotifier
from datetime import date, datetime
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
    urlFile = open('classesURL.json')
    data = json.load(myFile)
    date = get_date()

    for dayInstance in data:
        if dayInstance['day'] == date['day']:
            for myClass in dayInstance['clases']:
                for classInstance in urlFile:
                    if myClass['start'] == date['time']:
                        notif(myClass['nombre'], 'La clase empieza {}\nLa clase temina {}\nSuerte!'.format(myClass['start'], myClass['end']))
                        time.sleep(5)
                        if classInstance['name'] == myClass['name']:
                            open_in_browser(classInstance['url'])
                        print(myClass['nombre'])
                        time.sleep(65)
                    elif myClass['end'] == date['time']:
                        notif('Ha termidado la clase')
                        print("End")
                        time.sleep(65)

    myFile.close()

def main():
    date = get_date()
    while date['day'] != "Saturday" or date['day'] != "Sunday":
        read_json_file('schedule.json')


if __name__ == "__main__":
    print('Schedule manager\n[i] Active')
    main()