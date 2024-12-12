# -*- coding: utf-8 -*-

from __future__ import annotations

import logging as lg

from puffkit_example import __version__

from puffkit import PkApp


class ExampleApp(PkApp):
    def __init__(self):
        lg.basicConfig(
            format="%(asctime)s : %(levelname)-8s : %(threadName)s : %(filename)s:"
            "%(lineno)d : %(name)s :: %(message)s",
            level=lg.DEBUG,
        )

        super().__init__(
            app_name="ExampleApp",
            app_version=__version__,
            display_size=(800, 600),
            display_arguments={},
            internal_screen_size=(400, 300),
            fps_limit=60,
        )

        self.event_manager.add_handler("Quit", lambda _: self.quit())
