from Scanner import Scanner
from Analysis_controller import AnalysisController
from multiprocessing import Process, Lock
from Calculator import CoordinatesCalculator
from Logger import Logger


class DataGrabber:
    __scans = []
    __processes = []
    __mutex = Lock()

    @staticmethod
    def get_mutex():
        return DataGrabber.__mutex

    @staticmethod
    def get():
        response = []
        for scan in DataGrabber.__scans:
            entry = scan.get()
            entry.update({"id": DataGrabber.__scans.index(scan)})
            response.append(entry)
        return response

    @staticmethod
    def start_scan(coordinates):
        coordinates = CoordinatesCalculator.calculate(coordinates)
        for scan in DataGrabber.__scans:
            if scan.get() == coordinates['page']:
                return False
        new_scan = Scanner(coordinates['page'], coordinates['blocks'])
        Logger.log_scan_start(new_scan.__str__())
        p = Process(target=Scanner.start, args=(new_scan, DataGrabber.__mutex))
        p.start()
        # threading.Thread(target=new_scan.start).start()
        DataGrabber.__scans.append(new_scan)
        DataGrabber.__processes.append(p)
        AnalysisController.notify_started()
        AnalysisController.start(DataGrabber.__mutex)
        return True

    @staticmethod
    def stop_scan(id):
        Logger.log_scan_stop(DataGrabber.__scans[id].__str__())
        DataGrabber.__scans[id].stop()
        DataGrabber.__processes[id].terminate()
        del DataGrabber.__scans[id]
        del DataGrabber.__processes[id]
        if len(DataGrabber.__scans) == 0:
            AnalysisController.notify_ended()
