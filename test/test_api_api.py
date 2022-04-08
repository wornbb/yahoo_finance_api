# coding: utf-8

"""
    Yahoo Finance API Specification

    Real time low latency Yahoo Finance API for stock market, crypto currencies, and currency exchange  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import yahoo_client
from yahoo_client.yahoo_api.api_api import APIApi  # noqa: E501
from yahoo_client.rest import ApiException


class TestAPIApi(unittest.TestCase):
    """APIApi unit test stubs"""

    def setUp(self):
        self.api = APIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_autocomplete(self):
        """Test case for autocomplete

        """
        pass

    def test_chart(self):
        """Test case for chart

        """
        pass

    def test_history(self):
        """Test case for history

        """
        pass

    def test_insights(self):
        """Test case for insights

        """
        pass

    def test_options(self):
        """Test case for options

        """
        pass

    def test_popular(self):
        """Test case for popular

        """
        pass

    def test_quotes(self):
        """Test case for quotes

        """
        pass

    def test_similar(self):
        """Test case for similar

        """
        pass

    def test_stock_details(self):
        """Test case for stock_details

        """
        pass

    def test_summary(self):
        """Test case for summary

        """
        pass

    def test_trending(self):
        """Test case for trending

        """
        pass


if __name__ == '__main__':
    unittest.main()
