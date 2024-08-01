from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static


class NameDisplay(Static):
    """A widget to display name services."""

    # start_time = reactive(monotonic)
    # time = reactive(0.0)
    # total = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        # self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        """Method to update time to current."""
        # self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        # minutes, seconds = divmod(time, 60)
        # hours, minutes = divmod(minutes, 60)
        # self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start_watch(self) -> None:
        """Method to start watch service state."""
        # self.start_time = monotonic()
        # self.update_timer.resume()

    def stop_watch(self):
        """Method to stop watch service state."""
        # self.update_timer.pause()
        # self.total += monotonic() - self.start_time
        # self.time = self.total

    def restart_service(self):
        """Method to restart service."""
        # self.total = 0
        # self.time = 0


class Service(Static):
    """A service widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        name_display = self.query_one(NameDisplay)
        if button_id == "start_watch":
            name_display.start_watch()
            self.add_class("watch")
        elif button_id == "stop_watch":
            name_display.stop_watch()
            self.remove_class("watch")
        elif button_id == "restart_service":
            name_display.restart_service()

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Watch", id="start_watch", variant="success")
        yield Button("Stop", id="stop_watch", variant="error")
        yield Button("Restart", id="restart_service")
        yield NameDisplay()


class RestarterServices(App):
    """A RestarterServices app to manage services."""

    CSS_PATH = "restarter-services.css"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_service", "Add"),
        ("r", "remove_service", "Remove"),
    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        # yield ScrollableContainer(Stopwatch(), Stopwatch(), Stopwatch(), id="timers")
        yield ScrollableContainer(id="services")

    def action_add_service(self) -> None:
        """Called to add a service."""
        new_service = Service()
        self.query_one("#services").mount(new_service)
        new_service.scroll_visible()

    def action_remove_service(self) -> None:
        """Called to remove a service."""
        services = self.query("Service")
        if services:
            services.last().remove()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = RestarterServices()
    app.run()