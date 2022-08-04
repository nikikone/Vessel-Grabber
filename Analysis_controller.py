import time
from multiprocessing import Process
from Queue import Queue
from Analyzer import Analyzer
import threading
from Logger import Logger


class AnalysisController:
    __analyzers = []
    __has_scanners = False
    __in_work = False
    __processes = []
    __empty = False

    @staticmethod
    def start(mutex):
        if AnalysisController.__in_work:
            return
        AnalysisController.__in_work = True
        for i in range(1):
            analysis = Analyzer()
            AnalysisController.__analyzers.append(analysis)
        Logger.log_analysis_start()
        AnalysisController.__start_analysis(mutex)
        threading.Thread(target=AnalysisController.__check_file).start()
        return

    @staticmethod
    def __check_file():
        while True:
            if Queue.is_empty() and not AnalysisController.__has_scanners:
                AnalysisController.__stop_analysis()
                AnalysisController.__in_work = False
                return
            time.sleep(20)

    @staticmethod
    def __start_analysis(mutex):
        for analysis in AnalysisController.__analyzers:
            p = Process(target=Analyzer.start, args=(analysis, mutex))
            p.start()
            AnalysisController.__processes.append(p)
            # threading.Thread(target=analysis.start).start()
        return

    @staticmethod
    def __stop_analysis():
        Logger.log_analysis_stop()
        for analysis in AnalysisController.__analyzers:
            analysis.stop()
        while len(AnalysisController.__analyzers) > 0:
            del(AnalysisController.__analyzers[0])
        for process in AnalysisController.__processes:
            process.terminate()
        while len(AnalysisController.__processes) > 0:
            del(AnalysisController.__processes[0])
        return

    @staticmethod
    def notify_ended():
        AnalysisController.__has_scanners = False

    @staticmethod
    def notify_started():
        AnalysisController.__has_scanners = True
