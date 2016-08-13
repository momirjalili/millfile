#!/bin/python
# -*- coding: utf-8 -*-
#
# Schemas for validating input data
#
from marshmallow import Schema, fields, pprint


class ImageParamsSchema(Schema):
    height = fields.Integer()
    width = fields.Integer()
    progressive = fields.Boolean()
    crop = fields.Boolean()
    left = fields.Integer()
    top = fields.Integer()
    right = fields.Integer()
    bottom = fields.Integer()
    zoom = fields.Integer()