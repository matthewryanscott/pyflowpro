"""Tests for `pyflowpro.parmlist`."""

from nose.tools import raises

from pyflowpro.parmlist import Parmlist


class TestParmlist(object):

    def test_string(self):
        """`Parmlist.__str__` returns a parmlist-formatted string
        based on values in a dictionary."""
        parms = Parmlist(
            TRXTYPE='S',
            TENDER='C',
            PARTNER='PayPal',
            VENDOR='SuperMerchant',
            USER='SuperMerchant',
            PWD='x1y&=3',
            ACCT='5555444433332222',
            EXPDATE='0308',
            AMT='123.00',
            )
        expected = (
            '"'
            'ACCT=5555444433332222&'
            'AMT=123.00&'
            'EXPDATE=0308&'
            'PARTNER=PayPal&'
            'PWD[6]=x1y&=3&'
            'TENDER=C&'
            'TRXTYPE=S&'
            'USER=SuperMerchant&'
            'VENDOR=SuperMerchant'
            '"'
            )
        assert expected == str(parms)

    @raises(ValueError)
    def test_string_disallow_quotes(self):
        """Quotes are never allowed in parmlists."""
        parms = Parmlist(
            KEY='"value"',
            )
        str(parms)
