from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Select, Static, Input, Label, Button
from models.objects import Sphere, Triangle, Rectangle
from .newObject import NewObject

class Form(Static):
    __OBJECTS = {"Sphere": Sphere, "Triangle": Triangle, "Rectangle": Rectangle}

    def compose(self) -> ComposeResult:
        yield Button("+", variant="default", classes="add", id="add-button")
        yield NewObject(classes="hidden")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-button":
            self.children[1].toggle_class("hidden")