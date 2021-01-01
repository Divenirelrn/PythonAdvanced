import logging


logging.basicConfig(level=logging.WARNING,
                    filename="./log.txt",
                    filemode="a",
                    format="%(asctime)s-%(filename)s[line: %(lineno)d]-%(levelname)s: %(message)s")

logging.debug("This is bebug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")