from flask_restplus import Api
from flask import Blueprint

blueprint =Blueprint ('TextSummarizer',__name__)
from .ns_BertSummarizer import api as ns1
from .ns_SimilaritySummarizer import api as ns2

api = Api(blueprint)
api.add_namespace(ns1)
api.add_namespace(ns2)