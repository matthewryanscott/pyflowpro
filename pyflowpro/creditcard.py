from urllib2 import Request, urlopen
from uuid import uuid4

from pyflowpro.parmlist import Parmlist
from pyflowpro.headers import STANDARD_HEADERS


class Sale(object):

    timeout = 45

    def __init__(self, config, acct, expdate, amt, street, zip,
                 invnum=None, ponum=None):
        self.config = config
        self.request_id = uuid4()
        self.parms = parms = Parmlist(
            acct = acct,
            expdate = expdate,
            amt = amt,
            street = street,
            zip = zip,
            partner = config.partner,
            vendor = config.vendor,
            user = config.user,
            password = config.password,
            )
        if invnum is not None:
            parms['invnum'] = invnum
        if ponum is not None:
            parms['ponum'] = ponum
        
    def submit(self):
        headers = {
            'Content-Type': 'text/namevalue',
            'X-VPS-REQUEST-ID': self.request_id,
            'X-VPS-CLIENT-TIMEOUT': str(self.timeout),
            'X-VPS-VIT-CLIENT-CERTIFICATION-ID': self.config.clientid,
            }
        headers.update(STANDARD_HEADERS)
        print repr(self.parms)
        print str(self.parms)
        request = Request(
            url = self.config.url,
            data = str(self.parms),
            headers = headers,
            )
        response = urlopen(request)
        data = response.read()
        response.close()
        response_parms = Parmlist(data)
        return response_parms
