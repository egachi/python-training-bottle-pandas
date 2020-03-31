#!"c:\users\edisga\desktop\ta\training\oss-onboarding\app service python basics\code\python-training-bottle-pandas\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'ftfy==5.7','console_scripts','ftfy'
__requires__ = 'ftfy==5.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ftfy==5.7', 'console_scripts', 'ftfy')()
    )
