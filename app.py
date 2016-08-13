#!/bin/python
# -*- coding: utf-8 -*-
import falcon
from millfile.resources import ImageResource

api = falcon.API()
api.add_route('/image', ImageResource())