#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

from flask import Flask
from flask import request

PROJECT_ROOT = os.path.normpath(os.path.realpath(os.path.dirname(__file__)))
sys.path.insert(0, PROJECT_ROOT)

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)


# vim: filetype=python
