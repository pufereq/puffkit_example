# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import TYPE_CHECKING

from puffkit import PkScene, PkContainer
from puffkit.widget import PkWidget, PkLabelWidget, PkButtonWidget, PkTextInputWidget


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

        self.scene_label_container = PkContainer(
            self.app,
            self.surface,
            "SceneLabelContainer",
            (0, 0, 400, 16),
        )

        self.scene_label_container.add_widget(
            PkLabelWidget(
                "scene_label",
                self.scene_label_container,
                "Widget Test Scene",
                (0, 0, 400, 16),
                text_align="center",
                vertical_align="middle",
            ),
        )

        self.containers: list[PkContainer] = []

        container = PkContainer(
            self.app,
            self.surface,
            "TestContainer",
            (0, 16, 400, 284),
            draw_outline=True,
        )

        container.add_widget(
            PkLabelWidget(
                "test_label",
                container,
                "Test Container",
                (0, 0, 400, 16),
                text_align="center",
                vertical_align="middle",
            ),
        )

        container.add_widget(
            PkButtonWidget(
                "test_button",
                container,
                "Test Button",
                (16, 16, 64, 32),
                background_color="#000000",
                background_color_disabled="#888888",
                background_color_pressed="#606060",
                background_color_hovered="#404040",
                text_color="#FFFFFF",
            ),
        )

        container.add_widget(
            PkLabelWidget(
                "button_state_label",
                container,
                "Button state: ",
                (96, 16, 284, 32),
                text_align="left",
                vertical_align="middle",
            ),
        )

        container.add_widget(
            PkButtonWidget(
                "test_disabled_button",
                container,
                "Disabled",
                (16, 64, 64, 32),
                background_color="#000000",
                background_color_disabled="#888888",
                background_color_pressed="#606060",
                background_color_hovered="#404040",
                text_color="#FFFFFF",
                disabled=True,
            ),
        )

        # textbox widget
        container.add_widget(
            PkTextInputWidget(
                "test_textbox",
                container,
                (16, 112, 368, 32),
                "Test Textbox",
                padding=4,
                background_color="#000000",
                background_color_disabled="#888888",
                background_color_focused="#404040",
                text_color="#FFFFFF",
                placeholder="Type here...",
            ),
        )

        self.containers.append(container)

    def on_update(self, delta: float) -> None:
        """Update the scene."""
        button_states: list[str] = []
        button = self.containers[0].widgets["test_button"]
        if button._disabled:
            button_states.append("Disabled")
        if button._hovered:
            button_states.append("Hovered")
        if button._pressed:
            button_states.append("Pressed")
        if not button_states:
            button_states.append("Normal")
        self.containers[0].widgets["button_state_label"].set_text(
            f"Button state: {', '.join(button_states)}"
        )

        self.scene_label_container.input(**self._input)
        self.scene_label_container.update(delta)

        for container in self.containers:
            container.input(
                self._input["events"],
                self._input["keys"],
                self._input["mouse_pos"],
                self._input["mouse_buttons"],
            )
            container.update(delta)

    def on_render(self) -> None:
        """Render the scene."""
        self.surface.fill("#aaa")
        self.scene_label_container.render()

        for container in self.containers:
            container.render()
