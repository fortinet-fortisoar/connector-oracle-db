"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector
from .builtins import make_query


class OracleDB(Connector):

    def execute(self, config, operation, operation_params, **kwargs):
        operations = {'db_query': make_query}
        operation = operations.get(operation)
        config.pop('name', None)
        return operation(config, operation_params)

    def check_health(self, config):
        config.pop('name', None)
        query_string = 'select 1 from dual'
        make_query(config, {'query_string': query_string})