from datetime import datetime


class Logger:
    __filename = 'log.txt'

    @staticmethod
    def clear():
        open(Logger.__filename, 'w').close()

    @staticmethod
    def log_scan_start(scan):
        Logger.__log(f'Started scan at {scan}')

    @staticmethod
    def log_scan_stop(scan):
        Logger.__log(f'Stopped scan at {scan}')

    @staticmethod
    def log_ships(ship_num, scan):
        Logger.__log(f'Scan at {scan} got {ship_num} ships')

    @staticmethod
    def log_scan_error(scan, message):
        Logger.__log(f'Scan at {scan} got an error while scanning: {message}')

    @staticmethod
    def log_file_error(error_type):
        Logger.__log(f'Faced an error: {error_type}, while trying to access raw data')

    @staticmethod
    def log_analysis_start():
        Logger.__log('Started raw data analysis')

    @staticmethod
    def log_analysis_stop():
        Logger.__log('Stopped analysis')

    @staticmethod
    def log_analysis_wait():
        Logger.__log('Analyzer fell asleep. Cause: empty file \'raw_data\'')

    @staticmethod
    def log_db_error():
        Logger.__log('Faced an error while writing to db, skipping')

    @staticmethod
    def __log(message):
        with open(Logger.__filename, 'a') as f:
            log = f'{datetime.now()}: {message}\n'
            f.write(log)
            f.close()
