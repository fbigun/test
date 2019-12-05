#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import socket
from logging import StreamHandler
from logging.handlers import SysLogHandler
from rfc5424logging import Rfc5424SysLogHandler

rizhiyi_token = 'dc9cb7133e574ba792ea5d15f4d25312'

log = logging.getLogger('mylog')
log.setLevel(logging.DEBUG)

# log_hdlr=SysLogHandler(facility=SysLogHandler.LOG_LOCAL5, address='/dev/log')
# log_hdlr=SysLogHandler(
#  address=('log.u.rizhiyi.com', 5140),
#  facility=SysLogHandler.LOG_LOCAL5
#  )
log_hdlr = SysLogHandler(
  address=('tbjohufa.u.rizhiyi.com', 5140),
  facility=SysLogHandler.LOG_LOCAL5
  )
console = StreamHandler()

rsyslog = Rfc5424SysLogHandler(
  address=('log.u.rizhiyi.com', 5140),
  socktype=socket.SOCK_STREAM,
  structured_data={rizhiyi_token: {'tag': 'udp'}},
  enterprise_id=32473
  )


log_format = logging.Formatter(
  'hhl-%(name)s-server[%(process)d]-%(levelname)s: %(message)s'
  )
log_hdlr.setFormatter(log_format)
log_hdlr.setLevel(logging.ERROR)

console.setFormatter(log_format)
console.setLevel(logging.DEBUG)

log.addHandler(log_hdlr)
log.addHandler(console)
log.addHandler(rsyslog)

log.debug('debug message test')
log.error('error message test')
log.info('hello info test')
