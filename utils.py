from datetime import datetime


class Console:
    @staticmethod
    def sys(msg):
        print("[{}]: {}".format(datetime.now().strftime("%H:%M:%S"), msg))
