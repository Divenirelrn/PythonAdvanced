import urllib

url = "中国"
url_encode = urllib.parse.quote(url)
print(url_encode)

url_decode = urllib.parse.unquote(url_encode)
print(url_decode)

import logging

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s-%(filename)s[line: %(lineno)s]-%(levelname)s: %(message)s")

logging.warning("This is warning message")