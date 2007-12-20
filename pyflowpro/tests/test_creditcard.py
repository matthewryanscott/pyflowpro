"""Test the Transaction class."""

import config

from pyflowpro.creditcard import Sale


class TestCreditcardSale(object):

    def test_success(self):
        tx = Sale(
            config,
            acct='5105105105105100',
            expdate='0109',
            invnum='INV12345',
            amt='25.12',
            ponum='PO12345',
            street='123 Fake St.',
            zip='12345',
            )
        response = tx.submit()
        assert response['result'] == '0'
