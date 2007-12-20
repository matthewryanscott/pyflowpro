from pyflowpro.parmlist import Parmlist


class Sale(object):

    def __init__(self, config, acct, expdate, amt, street, zip,
                 invnum=None, ponum=None):
        self.config = config
        self.base_parms = base_parms = Parmlist(
            acct = acct,
            expdate = expdate,
            amt = amt,
            street = street,
            zip = zip,
            )
        if invnum is not None:
            base_parms['invnum'] = invnum
        if ponum is not None:
            base_parms['ponum'] = ponum
        
    def submit(self):
        pass
