class Parmlist(dict):

    def __init__(self, *args, **kw):
        super(Parmlist, self).__init__()
        # >0 positional args with >0 keyword args is ambiguous.
        if len(args) > 0 and len(kw) > 0:
            raise TypeError(
                'Provide either positional or keyword arguments, not both.')
        # >1 positional args is ambiguous.
        if len(args) > 1:
            raise TypeError('Provide only one positional argument.')
        if len(args) == 1:
            # Positional arg: convert to a dictionary.
            kw = _to_dict(args[0])
        self.update(kw)

    def __getitem__(self, key):
        return super(Parmlist, self).__getitem__(key.lower())

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
        super(Parmlist, self).__setitem__(key.lower(), value)

    def __str__(self):
        args = []
        for key, value in self.items():
            key = key.upper()
            if '=' in value or '&' in value:
                key = '%s[%d]' % (key, len(value))
            args.append('%s=%s' % (key, value))
        args.sort()
        return '"' + '&'.join(args) + '"'

    def copy(self):
        return Parmlist(**self)

    def update(self, other):
        # Update item-by-item so that __setitem__ rules are enforced.
        for key, value in other.iteritems():
            self[key] = value
        

BEGIN, NAME, LEN, VALUE, RESET, END = range(6)


def _to_dict(s):
    """Return a dictionary version of the parmlist string `s`."""
    # Not a very clever implementation, but used in production for a
    # couple of years, and not out to be a speed demon anyway.  Just a
    # simple state machine.  If anyone takes the time to implement a
    # regex version, please let me know!  -mscott
    result = {}
    state = BEGIN
    cur_name = ''
    cur_len_str = ''
    cur_len = 0
    cur_value = ''
    processed = ''
    for c in s:
        processed += c
        if state is BEGIN:
            if c is not '"':
                raise ValueError('String must begin with a double quote.')
            state = NAME
        elif state is NAME:
            if c.isalpha():
                cur_name += c
            elif c in '[]':
                state = LEN
            elif c is '=':
                state = VALUE
            else:
                raise ValueError('Error parsing string into values at %r.'
                                 % processed)
        elif state is LEN:
            if c.isdigit():
                cur_len_str += c
            elif c is ']':
                state = NAME
            else:
                raise ValueError('Error parsing string into values at %r.'
                                 % processed)
        elif state is VALUE:
            if cur_len_str:
                cur_len = int(cur_len_str)
                cur_len_str = ''
            if cur_len:
                cur_value += c
                cur_len -= 1
                if not cur_len:
                    state = RESET
                    continue
            elif c is '&':
                state = RESET
            elif c is '"':
                state = END
            else:
                cur_value += c
        elif state is RESET:
            if c is '"':
                state = END
        if state is RESET or state is END:
            result[cur_name] = cur_value
            cur_name = ''
            cur_len_str = ''
            cur_len = 0
            cur_value = ''
            if state is RESET:
                state = NAME
    if state is not END:
        raise ValueError('Premature end of string.')
    return result
