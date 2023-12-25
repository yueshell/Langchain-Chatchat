# -*- coding: utf8 -*-
# create_author: (heyue@g-i.asia)
import sys

DEFAULT_BIND_HOST = "0.0.0.0" if sys.platform != "win32" else "127.0.0.1"

print(DEFAULT_BIND_HOST)
