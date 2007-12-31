from urllib2 import Request, urlopen
from uuid import uuid4

from pyflowpro.parmlist import Parmlist
from pyflowpro.headers import STANDARD_HEADERS


class Sale(object):

    timeout = 45

    def __init__(self, config, acct, expdate, cvv2, amt, street, zip,
                 invnum=None, ponum=None):
        self.config = config
        self.request_id = uuid4()
        self.parms = parms = Parmlist(
            trxtype = 'S',              # [S]ale
            tender = 'C',               # [C]redit
            acct = str(acct),
            expdate = str(expdate),
            cvv2 = str(cvv2),
            amt = str(amt),
            street = str(street),
            zip = str(zip),
            partner = str(config.partner),
            vendor = str(config.vendor),
            user = str(config.user),
            pwd = str(config.password),
            )
        if invnum is not None:
            parms['invnum'] = invnum
        if ponum is not None:
            parms['ponum'] = ponum
        
    def submit(self):
        host = self.config.host
        url = 'https://' + host
        headers = {
            'Host': host,
            'X-VPS-REQUEST-ID': self.request_id,
            'X-VPS-CLIENT-TIMEOUT': str(self.timeout), # Doc says to do this
            'X-VPS-Timeout': str(self.timeout), # Example says to do this
            }
        headers.update(STANDARD_HEADERS)
        request = Request(
            url = url,
            data = str(self.parms),
            headers = headers,
            )
        response = urlopen(request)
        data = response.read()
        response.close()
        response_parms = Parmlist(data)
        return response_parms
