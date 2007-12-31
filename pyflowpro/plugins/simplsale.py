from pyflowpro import creditcard


class BaseCommerce(object):

    host = 'example.com'
    notice = 'Unconfigured BaseCommerce class.'
    
    SUCCESS = 0
    FAILURE = 1

    def __init__(self, config, values):
        self._partner = config['simplsale.commerce.partner']
        self._vendor = config['simplsale.commerce.vendor']
        self._user = config['simplsale.commerce.user']
        self._password = config['simplsale.commerce.password']
        self.values = values
        self.submitted = False

    def submit(self):
        if self.submitted:
            raise RuntimeError('Cannot re-submit %r.' % self)
        self.submitted = True
        # creditcard.Sale just needs a simple getattr-style object to
        # hold configuration, so create a one-off object subclass to
        # be that object.
        class config(object):
            host = self.host
            partner = self._partner
            vendor = self._vendor
            user = self._user
            password = self._password
        sale = creditcard.Sale(
            config = config,
            acct = self.values['billing_card_number'],
            expdate = (self.values['billing_expiration_month'] +
                       self.values['billing_expiration_year']),
            cvv2 = self.values['billing_cvv2'],
            amt = self.values['billing_amount_price'],
            street = self.values['billing_street'],
            zip = self.values['billing_zip'],
            )
        response = sale.submit()
        self.result_text = response['respmsg']
        if response['result'] == '0':
            self.result = self.SUCCESS
            self.number = response['pnref']
        else:
            self.result = self.FAILURE


class LiveCommerce(BaseCommerce):

    host = 'payflowpro.verisign.com'
    notice = None


class PilotCommerce(BaseCommerce):

    host = 'pilot-payflowpro.verisign.com'
    notice = 'Using Payflow Pro PILOT server.'
