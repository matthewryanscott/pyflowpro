class Parmlist(dict):

    def __init__(self, **kw):
        super(Parmlist, self).__init__()
        # Manually apply keyword args so they pass through __setitem__.
        for key, value in kw.iteritems():
            self[key] = value

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError('Key must be a string.')
        if not isinstance(value, str):
            raise KeyError('Value must be a string.')
        if '\n' in key:
            raise KeyError('Key must not contain newline.')
        if '"' in key:
            raise KeyError('Key must not have double quote.')
        if '\n' in value:
            raise ValueError('Value must not contain newline.')
        if '"' in value:
            raise ValueError('Value must not contain double quote.')
        super(Parmlist, self).__setitem__(key, value)

    def __str__(self):
        args = []
        for key, value in self.items():
            key = key.upper()
            if '=' in value or '&' in value:
                key = '%s[%d]' % (key, len(value))
            args.append('%s=%s' % (key, value))
        args.sort()
        return '"' + '&'.join(args) + '"'
