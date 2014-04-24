#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__file__))
from webapp.server import app

app.run()
