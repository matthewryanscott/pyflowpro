"""Tests for `pyflowpro.parmlist`."""

from nose.tools import raises

from pyflowpro.parmlist import Parmlist


class TestParmlist(object):

    def test_case_insensitive_keys(self):
        parms = Parmlist(foo='bar')
        parms['FOO'] = 'baz'
        assert parms['foo'] == 'baz'

    def test_copy(self):
        parms = Parmlist(foo='bar')
        copy = parms.copy()
        assert isinstance(parms, Parmlist)
        assert len(copy) == 1
        assert copy['FOO'] == 'bar'

    def test_fromstring(self):
        parms = Parmlist(
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
        expected = Parmlist(
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
        assert parms == expected

    def test_tostring(self):
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

    @raises(KeyError)
    def test_disallow_key_newlines(self):
        """Newlines are never allowed in parmlist keys."""
        parms = Parmlist()
        parms['key\n'] = 'value'

    @raises(KeyError)
    def test_disallow_key_nonstring(self):
        """Non-strings are never allowed in parmlist keys."""
        parms = Parmlist()
        parms[u'key'] = 'value'

    @raises(KeyError)
    def test_disallow_key_quotes(self):
        """Quotes are never allowed in parmlist keys."""
        parms = Parmlist()
        parms['key"'] = 'value'

    @raises(ValueError)
    def test_disallow_value_newlines(self):
        """Newlines are never allowed in parmlist values."""
        parms = Parmlist(
            KEY='value\n',
            )

    @raises(KeyError)
    def test_disallow_value_nonstring(self):
        """Non-strings are never allowed in parmlist values."""
        parms = Parmlist(
            KEY=u'value',
            )

    @raises(ValueError)
    def test_disallow_value_quotes(self):
        """Quotes are never allowed in parmlist values."""
        parms = Parmlist(
            KEY='"value"',
            )

