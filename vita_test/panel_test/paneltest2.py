import panel as pn
import numpy as np
import holoviews as hv
import inspect
import sys

# Enable Panel extensions
pn.extension()

# Create a simple sine wave plot
def sine_wave(frequency, amplitude, phase):
    x = np.linspace(0, 10, 500)
    y = amplitude * np.sin(frequency * x + phase)
    return hv.Curve((x, y)).opts(width=600, height=400, title="Sine Wave")

# Create interactive widgets
frequency = pn.widgets.FloatSlider(name="Frequency", start=0.1, end=2, step=0.1, value=1)
amplitude = pn.widgets.FloatSlider(name="Amplitude", start=0.1, end=2, step=0.1, value=1)
phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi*2, step=0.1, value=0)

# Create a panel that updates the plot based on the widget values
@pn.depends(frequency, amplitude, phase)
def update_plot(freq, amp, ph):
    return sine_wave(freq, amp, ph)

# Create a chat interface
class ChatInterface:
    def __init__(self):
        self.messages = []
        self.input = pn.widgets.TextInput(placeholder="Type a message...")
        self.send_button = pn.widgets.Button(name="Send", button_type="primary")
        self.chat_pane = pn.pane.Markdown("")
        self.send_button.on_click(self.add_message)

    def add_message(self, event):
        if self.input.value:
            self.messages.append(f"User: {self.input.value}")
            self.messages.append(f"Bot: You said: '{self.input.value}'. "
                                 f"The current sine wave parameters are: "
                                 f"Frequency={frequency.value:.2f}, "
                                 f"Amplitude={amplitude.value:.2f}, "
                                 f"Phase={phase.value:.2f}")
            self.chat_pane.object = "\n\n".join(self.messages)
            self.input.value = ""

    def get_panel(self):
        return pn.Column(
            self.chat_pane,
            pn.Row(self.input, self.send_button)
        )

# Instantiate the chat interface
chat = ChatInterface()

# Function to get the source code
def get_source_code():
    module = sys.modules[__name__]
    source = inspect.getsource(module)
    return f"```python\n{source}\n```"

# Create a Panel object for the source code
source_code_pane = pn.pane.Markdown(get_source_code())

# Create the dashboard layout
dashboard = pn.Column(
    pn.pane.Markdown("# Interactive Sine Wave Dashboard with Chat and Source Code"),
    pn.Row(
        pn.Column(
            pn.pane.Markdown("## Chat"),
            chat.get_panel(),
            width=400
        ),
        pn.Column(
            pn.pane.Markdown("## Sine Wave Graph"),
            pn.pane.Markdown("Adjust the sliders to change the sine wave parameters:"),
            frequency,
            amplitude,
            phase,
            update_plot,
            width=500
        ),
        pn.Column(
            pn.pane.Markdown("## Source Code"),
            source_code_pane,
            width=500
        )
    )
)

# Show the dashboard
dashboard.servable()