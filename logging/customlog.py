import logging

fmtstr="User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"
extdata = {"user": "user@example.com"}

logging.basicConfig(filename="output.log", 
                    level=logging.DEBUG, 
                    format=fmtstr,
                    datefmt = datestr)

def another_func():
    logging.debug("This is a debug-level log message", extra=extdata)

logging.info("This is an info-level log message", extra=extdata)
logging.warning("this is a warning-level message", extra=extdata)
another_func()

