import time
from Request import Request
import requests
from Queue import Queue
from Logger import Logger


class Scanner(object):

    def __init__(self, page, blocks):
        self.__status = True
        self.__requests = Request(page, blocks)
        self.__coords = page
        self.__test = self.__requests.api
        # self.start()

    def __str__(self):
        return f"x:{self.__coords['x']}, y:{self.__coords['y']}, z:{self.__coords['z']}"

    def __repr__(self):
        return self.__coords

    def get(self):
        return self.__coords

    def start(self, mutex):
        self.__scan(mutex)

    def __scan(self, mutex):
        while self.__status:
            try:
                page = requests.get(url=self.__requests.page['url'], headers=self.__requests.page['headers'])
                if not page.status_code == 200:
                    Logger.log_scan_error(self.__str__(), 'faced connection error, will retry in 10 seconds')
                    time.sleep(10)
                    continue
                # print(self.__requests.page)
                # print(self.__test)
            except requests.exceptions.ConnectionError:
                Logger.log_scan_error(self.__str__(), 'faced connection error, will retry in 10 seconds')
                time.sleep(10)
                continue
            for i in range(12):
                for block in self.__test:
                    try:
                        data = requests.get(url=block['url'], headers=block['headers'])
                        if not data.status_code == 200:
                            Logger.log_scan_error(self.__str__(), 'faced API connection error, will retry in 10 seconds')
                            time.sleep(10)
                            continue
                    except requests.exceptions.ConnectionError:
                        Logger.log_scan_error(self.__str__(), 'faced API connection error, will retry in 10 seconds')
                        time.sleep(10)
                        continue
                    Logger.log_ships(data.json()['data']['areaShips'], self.__str__())
                    useful_data = self.__convert(data.json())
                    for ship in useful_data:
                        Queue.add(ship, mutex)
                time.sleep(10)

    @staticmethod
    def __convert(data):
        ship_data = []
        ships = data['data']
        for ship in ships['rows']:
            ship_data.append(ship)
        return ship_data

    def stop(self):
        self.__status = False