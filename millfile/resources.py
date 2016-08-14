#!/bin/python
# -*- coding: utf-8 -*-
#
# This file contains all the resources of the project
#
import falcon
from PIL import Image
import urllib
import StringIO
import io
from schemas import ImageParamsSchema
from libs.utils import mimetype


class ImageResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        schema = ImageParamsSchema()
        parsed_params = schema.load(req.params)
        if parsed_params.errors:
            raise falcon.HTTPBadRequest("Malformed params",
                                        str(parsed_params.errors))
        data = parsed_params.data
        image = Image.open(
            StringIO.StringIO(urllib.urlopen(data['url']).read()))
        image_mimetype = mimetype(image.format)

        resp.status = falcon.HTTP_200
        resp.content_type = image_mimetype
        image = image.resize(
            (data.get('width',image.size[0]),
            data.get('height',image.size[1]))
        )

        with io.BytesIO() as output:
            image.save(output, data.get('format', 'png').upper())
            resp.stream = output.getvalue()
            output.close()


