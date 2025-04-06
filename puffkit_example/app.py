# -*- coding: utf-8 -*-

from __future__ import annotations

import logging as lg

from puffkit_example import __version__

from puffkit import PkApp

from puffkit_example.scenes import WidgetTestScene


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

        self.event_manager.add_handler("QUIT", lambda _: self.quit())

        self.scene_manager.add_scene(WidgetTestScene(self))
        self.scene_manager.set_scene("WidgetTestScene")
