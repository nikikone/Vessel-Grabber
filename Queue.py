import json
import os
import pathlib
from Logger import Logger


directory = pathlib.Path().resolve()


class Queue:
    __file_name = "raw_data.gb"

    @staticmethod
    def add(ship, mutex):
        mutex.acquire()
        f = open(Queue.__file_name, 'a')
        f.write(json.dumps(ship) + '\n')
        f.close()
        mutex.release()

    @staticmethod
    def take(mutex):
        mutex.acquire()
        if not Queue.is_empty():
            with open(Queue.__file_name, 'r') as f:
                data = f.read().splitlines(True)
                ship = data[0]
                f.close()
            try:
                with open(Queue.__file_name, "w") as f:
                    f.writelines(data[1:])
                    f.close()
            except FileNotFoundError:
                Logger.log_file_error('FileNotFound')
            except OSError:
                Logger.log_file_error('OSError')
            mutex.release()
            try:
                answer = json.loads(ship)
            except ValueError:
                Logger.log_file_error('ValueError')
                answer = None
            return answer
        else:
            mutex.release()
            return None

    @staticmethod
    def is_empty():
        if not os.path.isfile(os.path.abspath(Queue.__file_name)):
            return True
        return os.path.getsize(os.path.abspath(Queue.__file_name)) == 0
