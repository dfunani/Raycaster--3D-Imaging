from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Select, Static, Input, Label, Button, ListItem
from models.objects import Sphere, Triangle, Rectangle
from models.types.objects import Vector3
from uuid import uuid4


class NewObject(Static):
    __OBJECTS = {"Sphere": Sphere, "Triangle": Triangle, "Rectangle": Rectangle}
    NEWOBJECTS = []

    def compose(self) -> ComposeResult:
        yield Select(
            ((key, key) for key in self.__OBJECTS.keys()),
            prompt="Select Object",
            allow_blank=False,
        )
        # yield Label("Position", classes="form-labels")
        yield Horizontal(
            Label("X:"),
            Input(placeholder="Enter X Position", classes="position"),
            Label("Y:"),
            Input(placeholder="Enter Y Position", classes="position"),
            Label("Z:"),
            Input(placeholder="Enter Z Position", classes="position"),
        )
        # yield Label("Size", classes="form-labels")
        yield Horizontal(
            Label("Radius:"),
            Input(placeholder="Enter Sphere Radius", classes="position"),
            Label("Width:"),
            Input(placeholder="Enter Width", classes="position"),
            Label("Height:"),
            Input(placeholder="Enter Height", classes="position"),
        )
        # yield Label("Color", classes="form-labels")
        yield Horizontal(
            Label("Red:"),
            Input(placeholder="Enter Red Value", classes="position"),
            Label("Green:"),
            Input(placeholder="Enter Green Value", classes="position"),
            Label("Blue:"),
            Input(placeholder="Enter Blue Value", classes="position"),
        )

        yield Button("Add Object", classes="add-object")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        selection = self.__OBJECTS[self.children[0].value](
                position=Vector3(
                    float(self.children[1].children[1].value),
                    float(self.children[1].children[3].value),
                    float(self.children[1].children[5].value),
                ),  # Position of the sphere
                radius=float(self.children[2].children[1].value),
                width=float(self.children[2].children[3].value),
                height=float(self.children[2].children[5].value),
                surfaceColor=Vector3(
                    float(self.children[3].children[1].value),
                    float(self.children[3].children[3].value),
                    float(self.children[3].children[5].value),
                ),  # Green color
                emissionColor=Vector3(
                    float(self.children[3].children[1].value),
                    float(self.children[3].children[3].value),
                    float(self.children[3].children[5].value),
                ),  # No emission
            )
        self.NEWOBJECTS.append(selection)

        listNodes = list(map(lambda x: ListItem(Horizontal(Label(str(x)), Button("X", classes="delete"))), self.NEWOBJECTS))
        self.parent.parent.query_one("#listed").remove_children()
        self.parent.parent.query_one("#listed")._add_children(*listNodes)