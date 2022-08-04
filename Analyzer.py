import json
import time

from Queue import Queue
from ShipMap import shipType_map, shipAttrs_map
from DBHook import DBHook
from Logger import Logger
from Input_db import Input_db


class Analyzer(object):

    def __init__(self):
        self.__status = True

    def start(self, mutex):
        self.__analyze(mutex)

    def stop(self):
        self.__status = False

    def __analyze(self, mutex):
        num = 0
        while self.__status:
            ship = self.__grab(mutex)
            if ship is None:
                continue
            num += 1
            ship = self.__refine(ship)
            if ship is None:
                continue
            if not self.__validate(ship):
                continue
            relevance = self.__is_relevant(ship)
            if ship['name'] == '[SAT-AIS]':
                if relevance == 0:
                    if not DBHook.add_ais(ship):
                        continue
                    Analyzer.__send(ship)
                elif relevance == 1:
                    if not DBHook.update_ais(ship):
                        continue
                    Analyzer.__send(ship)
            else:
                if relevance == 0:
                    if not DBHook.add(ship):
                        continue
                    Analyzer.__send(ship)
                    # print('record: ' + str(num))
                elif relevance == 1:
                    if not DBHook.update(ship):
                        continue
                    Analyzer.__send(ship)
                    # print('record: ' + str(num))


    @staticmethod
    def __grab(mutex):
        if Queue.is_empty():
            Logger.log_analysis_wait()
            time.sleep(10)
            return None
        ship = Queue.take(mutex)
        return ship

    @staticmethod
    def __refine(ship):
        if 'SHIPNAME' not in ship:
            return None
        if ship['SHIPNAME'] == '[SAT-AIS]':
            ship = Analyzer.__refine_ais(ship)
            return ship
        if 'ELAPSED' in ship:
            ship.pop("ELAPSED")
        if "L_FORE" in ship:
            ship.pop("L_FORE")
        if 'W_LEFT' in ship:
            ship.pop("W_LEFT")
        if "GT_SHIPTYPE" in ship:
            ship.pop("GT_SHIPTYPE")
        ship = {shipAttrs_map[k].lower() if k in shipAttrs_map else k.lower(): v for k, v in ship.items()}
        if ship['type'] in shipType_map:
            ship.update({'type': shipType_map[ship['type']]})
        else:
            # print('\nНОВЫЙ ТИП:')
            # print(ship)
            ship.update({'type': "skip"})
        return ship

    @staticmethod
    def __refine_ais(ship):
        if 'TYPE_IMG' in ship:
            ship.pop('TYPE_IMG')
        if 'TYPE_NAME' in ship:
            ship.pop('TYPE_NAME')
        if 'STATUS_NAME' in ship:
            ship.pop('STATUS_NAME')
        ship = {shipAttrs_map[k].lower() if k in shipAttrs_map else k.lower(): v for k, v in ship.items()}
        if ship['type'] in shipType_map:
            ship.update({'type': shipType_map[ship['type']]})
        return ship

    @staticmethod
    def __validate(ship):
        if ship['name'] == '[SAT-AIS]':
            return Analyzer.__validate_ais(ship)
        integrity = True
        if not all(key in ship for key in ('latitude',
                                           'longitude',
                                           'speed',
                                           'heading',
                                           'destination',
                                           'flag',
                                           'length',
                                           'name',
                                           'type',
                                           'id',
                                           'width')):
            integrity = False
        for k, v in ship.items():
            if k in ('destination', 'course', 'deadweight', 'heading', 'rotation'):
                continue
            if v is None:
                integrity = False
                break
        if ship['type'] == "skip":
            integrity = False
        if 'course' not in ship:
            ship.update({"course": None})
        if "deadweight" not in ship:
            ship.update({'deadweight': None})
        if 'rotation' not in ship:
            ship.update({'rotation': None})
        return integrity

    @staticmethod
    def __validate_ais(ship):
        integrity = True
        if not all(key in ship for key in ('latitude',
                                           'longitude',
                                           'speed',
                                           'heading',
                                           'type',
                                           'id')):
            integrity = False
        if ship['type'] == "skip":
            integrity = False
        return integrity

    @staticmethod
    def __is_relevant(ship):
        if ship['name'] == '[SAT-AIS]':
            return Analyzer.__is_relevant_ais(ship)
        # 0 - записи нет
        # 1 - обновить запись
        # 2 - неактульно
        record = DBHook.get(ship['id'])
        if record is None:
            return 0
        for k, v in ship.items():
            if k == 'latitude' or k == 'longitude':
                if round(float(v), 4) != round(float(record[k]), 4):
                    # print(k)
                    # print(' data: ' + str(v) + ' record:' + str(record[k]))
                    return 1
            # else:
            #     if v != record[k]:
            #         print(k)
            #         print(' data: '+ str(v) +' record:' + str(record[k]))
            #         return 1
        return 2


        # elif not ship == record:
        #     return 1
        # else:
        #     return 2

    @staticmethod
    def __is_relevant_ais(ship):
        record = DBHook.get_ais(ship['id'])

        if record is None:
            return 0
        for k, v in ship.items():
            if k == 'latitude' or k == 'longitude':
                if round(float(v), 4) != round(float(record[k]), 4):
                    # print(k)
                    # print(' data: ' + str(v) + ' record:' + str(record[k]))
                    return 1
        return 2

    @staticmethod
    def __send(ship):
        data = Analyzer.__convert_to_db_format(ship)
        Input_db.input_for_base(data)
        #Analyzer.__test(data)
        return

    @staticmethod
    def __test(ship):
        f = open('test.txt', 'a')
        f.write(json.dumps(ship))
        f.write('\n')
        f.close()
        return

    @staticmethod
    def __convert_to_db_format(ship):
        data = {}
        if ship['name'] == '[SAT-AIS]':
            data.update({'ship': None})
            record = {
                'id': ship['id'],
                'latitude': ship['latitude'],
                'longitude': ship['longitude'],
                'speed': ship['speed'],
                'course': ship['course'],
                'heading': ship['heading'],
                'type': ship['type']
            }
            data.update({'mark': record})
        else:
            record = {
                'id': ship['id'],
                'flag': ship['flag'],
                'length': ship['length'],
                'width': ship['width'],
                'name': ship['name'],
                'type': ship['type'],
            }
            data.update({'ship': record})
            record = {
                'latitude': ship['latitude'],
                'longitude': ship['longitude'],
                'speed': ship['speed'],
                'course': ship['course'],
                'heading': ship['heading'],
                'destination': ship['destination'],
                'deadweight': ship['deadweight']
            }
            data.update({'mark': record})
        return data
