#!/bin/python
# -*- coding: utf-8 -*-
#
# Schemas for validating input data
#
from marshmallow import Schema, fields, pprint


class ImageParamsSchema(Schema):
    url = fields.String(required=True)
    format = fields.String()
    height = fields.Integer()
    width = fields.Integer()
    progressive = fields.Boolean()
    crop = fields.Boolean()
    left = fields.Integer()
    upper = fields.Integer()
    right = fields.Integer()
    lower = fields.Integer()