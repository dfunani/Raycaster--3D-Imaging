from textual.app import App, ComposeResult
from textual.widgets import Header, Button, Label, ListView, ListItem
from textual.containers import Horizontal

from simulators.raycasters import render
from .components.form import Form
from .components.newObject import NewObject

class Main(App):
    objects = []
    """Manages the running of the textual componennt of the Raycaster app

    Args:
        App (Class): The base class for Textual Applications.
    """

    CSS_PATH = "styles/global.tcss"

    BINDINGS = [("return", "toggle_dark", "Toggles the Dark and Light modes")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Label(
            """Welcome to Raycaster 1.0, where ypu define primitive shapes 
to render on a 2D canvas and export as an image""",
            classes="introLabel",
        )
        yield Label("""Would you like to add an object?""", classes="queryLabel")
        yield Form()
        yield ListView(
            id="listed"
        )
        yield Button("Export", variant="primary", classes="export", id="export-button")

    def on_mount(self) -> None:
        self.title = "Raycaster"
        self.sub_title = "Simple 3D Imaging"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "export-button":
            render(list(NewObject.NEWOBJECTS), "object-export")
            
                
