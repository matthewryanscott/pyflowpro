"""Test the Transaction class."""

import config

from pyflowpro.creditcard import Sale


class TestCreditcardTransaction(object):

    def test_success(self):
        tx = Sale(
            acct='5105105105105100',
            expdate='0109',
            invnum='INV12345',
            amt='25.12',
            ponum='PO12345',
            street='123 Fake St.',
            zip='12345',
            user=config.user,
            vendor=config.vendor,
            partner=config.partner,
            pwd=config.password,
            )
