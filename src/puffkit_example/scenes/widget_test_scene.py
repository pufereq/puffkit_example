# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import TYPE_CHECKING

from puffkit import PkScene, PkContainer
from puffkit.widget import (
    PkWidget,
    PkLabelWidget,
    PkButtonWidget,
    PkTextInputWidget,
    PkImageWidget,
)
from puffkit.image import PkImage


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
            (0, 0, 800, 32),
        )

        self.scene_label_container.add_widget(
            PkLabelWidget(
                "scene_label",
                self.scene_label_container,
                "Widget Test Scene",
                (0, 0, 800, 32),
                text_align="center",
                vertical_align="middle",
            ),
        )

        self.containers: list[PkContainer] = []

        container = PkContainer(
            self.app,
            self.surface,
            "TestContainer",
            (0, 32, 800, 568),
            draw_outline=True,
        )

        container.add_widget(
            PkLabelWidget(
                "test_label",
                container,
                "Test Container",
                (0, 0, 800, 32),
                text_align="center",
                vertical_align="middle",
            ),
        )

        container.add_widget(
            PkButtonWidget(
                "test_button",
                container,
                "Test Button",
                (32, 32, 128, 64),
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
                (192, 32, 568, 64),
                text_align="left",
                vertical_align="middle",
            ),
        )

        container.add_widget(
            PkButtonWidget(
                "test_disabled_button",
                container,
                "Disabled",
                (32, 128, 128, 64),
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
                (32, 224, 736, 64),
                "Test Textbox",
                padding=4,
                background_color="#000000",
                background_color_disabled="#888888",
                background_color_focused="#404040",
                text_color="#FFFFFF",
                placeholder="Type here...",
            ),
        )

        # image widgets
        # stretch
        container.add_widget(
            PkImageWidget(
                "test_image_widget_stretch",
                container,
                # PkImage.from_file("example_image.png", "assets/example_image.png"),
                PkImage.from_file("pawcio2.png", "assets/pawcio2.png"),
                (32, 320, 256, 96),
                "stretch",
            )
        )
        container.add_widget(
            PkLabelWidget(
                "stretch_label",
                container,
                "stretch",
                (32, 416, 256, 24),
                text_align="center",
                vertical_align="top",
            ),
        )
        # fit
        container.add_widget(
            PkImageWidget(
                "test_image_widget_fit",
                container,
                # PkImage.from_file("example_image.png", "assets/example_image.png"),
                PkImage.from_file("pawcio2.png", "assets/pawcio2.png"),
                (320, 320, 256, 96),
                "fit",
            )
        )
        container.add_widget(
            PkLabelWidget(
                "fit_label",
                container,
                "fit",
                (320, 416, 256, 24),
                text_align="center",
                vertical_align="top",
            ),
        )
        # fill
        container.add_widget(
            PkImageWidget(
                "test_image_widget_fill",
                container,
                # PkImage.from_file("example_image.png", "assets/example_image.png"),
                PkImage.from_file("pawcio2.png", "assets/pawcio2.png"),
                (32, 448, 256, 96),
                "fill",
            )
        )
        container.add_widget(
            PkLabelWidget(
                "fill_label",
                container,
                "fill",
                (32, 544, 256, 24),
                text_align="center",
                vertical_align="top",
            ),
        )
        # none
        container.add_widget(
            PkImageWidget(
                "test_image_widget_none",
                container,
                PkImage.from_file("pawcio2.png", "assets/pawcio2.png"),
                (320, 448, 256, 96),
                None,
            )
        )
        container.add_widget(
            PkLabelWidget(
                "none_label",
                container,
                "none",
                (320, 544, 256, 24),
                text_align="center",
                vertical_align="top",
            ),
        )
        # tile
        container.add_widget(
            PkImageWidget(
                "test_image_widget_tile",
                container,
                PkImage.from_file("pawcio2.png", "assets/pawcio2.png"),
                (608, 320, 160, 224),
                "tile",
            )
        )
        container.add_widget(
            PkLabelWidget(
                "tile_label",
                container,
                "tile",
                (608, 544, 160, 24),
                text_align="center",
                vertical_align="top",
            )
        )

        self.containers.append(container)

    def on_update(self, delta: float) -> None:
        """Update the scene."""
        button_states: list[str] = []
        button = self.containers[0].widgets["test_button"]
        if button.disabled:
            button_states.append("Disabled")
        if button.hovered:
            button_states.append("Hovered")
        if button.pressed:
            button_states.append("Pressed")
        if not button_states:
            button_states.append("Normal")
        self.containers[0].get_widget("button_state_label").set_text(
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
