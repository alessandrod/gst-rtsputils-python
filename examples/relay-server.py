#!/usr/bin/env python

import os
import sys
git = os.path.join(os.getcwd(), '.git')
if os.path.exists(git):
    sys.path.insert(0, os.getcwd())

from urlparse import urlparse
import gobject
gobject.threads_init()

import pygst
pygst.require("0.10")
from gst.rtspserver import Server
from rtsputils import RelayMediaFactory

local_url = sys.argv[1]
remote_url = sys.argv[2]

server = Server()
server.set_service(str(urlparse(local_url).port))

factory = RelayMediaFactory()
factory.props.location = remote_url
factory.set_shared(True)

mapping = server.get_media_mapping()
mapping.add_factory("/relay", factory)

server.attach()

loop = gobject.MainLoop()
loop.run()
