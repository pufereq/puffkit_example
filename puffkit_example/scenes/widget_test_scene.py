# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import TYPE_CHECKING

from puffkit import PkScene, PkContainer
from puffkit.widget import PkWidget, PkLabelWidget


if TYPE_CHECKING:
    from puffkit import PkApp


class WidgetTestScene(PkScene):
    """A scene to test the PkContainer and PkWidget classes."""

    def __init__(self, app: PkApp):
        """Initialize the scene.

        Args:
            app (PkApp): The main application object.
        """
        super().__init__("WidgetTestScene", app, lazy=True, auto_unload=True)

    def on_load(self) -> None:
        """Load the scene."""
        self.containers: list[PkContainer] = []

        self.containers.append(
            PkContainer(
                self.app,
                self.surface,
                "TestSceneContainer",
                (100, 100, 200, 150),
                draw_outline=True,
            )
        )

        self.containers.append(
            PkContainer(
                self.app,
                self.surface,
                "TestSceneContainer2",
                (50, 25, 150, 200),
                draw_outline=True,
            )
        )

        self.containers[0].add_widget(
            PkLabelWidget(
                self.containers[0],
                "KOCHAM AJAJX QJERY " * 100,
                (10, 10, 180, 100),
                text_align="center",
            )
        )

    def on_render(self) -> None:
        """Render the scene."""
        for container in self.containers:
            container.render()
