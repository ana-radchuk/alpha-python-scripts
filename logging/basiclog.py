import logging

# add debug logging to be ouput on console
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

logging.debug("This is a debug-level message")
logging.info("This is an info-level message")
logging.warning("This is a warning-level message")
logging.error("This is an error-level message")
logging.critical("This is a critical-level message")

x = "string"
y = 10
logging.info(f"Here's a {x} variable and int: {y}")