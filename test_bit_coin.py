import unittest
from unittest import TestCase
from unittest.mock import patch

import bit_coin

class TestBitCoin(Testcase):

    @patch('bit_coin.get_requests')# test response for get requests()
    def test_get_requests(self, mock_coins):
        mock_coins = 30
        api_response = {"USD":{"code":"USD","symbol":"&#36;","rate":"12,024.9550","description":"United States Dollar","rate_float":12024.955}}
        mock_coins.side_effect = [api_response]
        expected = 20
        self.assertEqual(expected)
