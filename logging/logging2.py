import logging


logger = logging.getLogger()
logger.setLevel(logging.WARNING)

fh = logging.FileHandler("./log.txt", mode="w")
fh.setLevel(logging.WARNING)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s-%(filename)s[line: %(lineno)d]-%(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.warning("This is warning message")
logger.error("This is error message")