import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import (
    DBSession,
    Base,
    )
	
from ..models import User

# Import the CryptContext class for hashing
from passlib.context import CryptContext

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

pass_contxt = CryptContext(
	schemes = ["sha512_crypt"],
	default = "sha512_crypt"
)

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
	
    with transaction.manager:
        admin = User(username=u'one', password=pass_contxt.encrypt(u'admin'))
        DBSession.add(admin)
