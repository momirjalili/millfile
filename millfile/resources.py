#!/bin/python
# -*- coding: utf-8 -*-
#
# This file contains all the resources of the project
#
import falcon
from schemas import ImageParamsSchema
from PIL import Image


class ImageResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        schema = ImageParamsSchema()
        parsed_params = schema.dumps(req.params)
        if parsed_params.errors:
            raise falcon.HTTPBadRequest("Malformed params",
                                        str(parsed_params.errors))
        resp.status = falcon.HTTP_200
        resp.body = parsed_params.data