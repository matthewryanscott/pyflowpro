import sys

from pyflowpro import version


STANDARD_HEADERS = {
    'X-VPS-INTEGRATION-PRODUCT': 'PyFlowPro',
    'X-VPS-INTEGRATION-VERSION': version.NUMBER,
    'X-VPS-VIT-OS-NAME': sys.platform,
    'Connection': 'close',
    'Content-Type': 'text/namevalue',
    }
