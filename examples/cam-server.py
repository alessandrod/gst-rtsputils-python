#!/usr/bin/env python

import os
import sys
git = os.path.join(os.getcwd(), '.git')
if os.path.exists(git):
    sys.path.insert(0, os.getcwd())

import gobject
gobject.threads_init()

import pygst
pygst.require("0.10")
from gst.rtspserver import Server, MediaMapping, MediaFactory
from rtsputils import CamMediaFactory

server = Server()
server.set_service("8554")

factory = CamMediaFactory()
factory.props.video = True
factory.props.audio = False
factory.props.video_width = 320
factory.props.video_height = 240
factory.props.video_codec = "theora"
factory.set_shared(True)

mapping = server.get_media_mapping()
mapping.add_factory("/ciao", factory)

server.attach()

loop = gobject.MainLoop()
loop.run()
