# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:52:56 2023

@author: donghwan0206
"""

from eod.request_handler_class import RequestHandler

class SymbolChangeHistory(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_SYMBOL_CHANGE_HISTORY = 'https://eodhistoricaldata.com/api/symbol-change-history/'
        super().__init__(api_key, timeout)

    def get_symbol_change_history(self, **query_params):
        """
        Get symbol change history you should use the following URL (only US exchanges are supported nowe.

        Parameters
        ----------
        **query_params :
            query_params.

        Returns
        -------
        list
            List of symbol change history data

        """
        self.endpoint = self.URL_SYMBOL_CHANGE_HISTORY
        return super().handle_request(self.endpoint, query_params)
