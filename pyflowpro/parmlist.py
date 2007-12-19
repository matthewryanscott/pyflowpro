class Parmlist(dict):

    def __init__(self, **kw):
        super(Parmlist, self).__init__(**kw)

    def __str__(self):
        args = []
        for key, value in self.items():
            key = key.upper()
            # XXX: Do some better filtration on init/getitem/setitem,
            # not here in __str__
            if '\n' in value:
                raise ValueError('Values must not contain line breaks.')
            if '"' in value:
                raise ValueError('Values must not contain line breaks.')
            if '=' in value or '&' in value:
                key = '%s[%d]' % (key, len(value))
            args.append('%s=%s' % (key, value))
        args.sort()
        return '"' + '&'.join(args) + '"'
