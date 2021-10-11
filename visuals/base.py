import panel as pn
import param

import pathlib

SNIPPETS_ROOT = pathlib.Path(__file__).parent.parent / "snippets"

ACCENT_BASE_COLOR = "#6082A2"

SVG = """
<svg xmlns="http://www.w3.org/2000/svg" width="54" height="14" viewBox="0 0 54 14"><g fill="none" fill-rule="evenodd" transform="translate(1 1)"><circle cx="6" cy="6" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width=".5"></circle><circle cx="26" cy="6" r="6" fill="#FFBD2E" stroke="#DEA123" stroke-width=".5"></circle><circle cx="46" cy="6" r="6" fill="#27C93F" stroke="#1AAB29" stroke-width=".5"></circle></g></svg>
"""

COMMAND="""
panel serve script.py --autoreload --show

Panel app running at: http://localhost:5006/panel
"""

class CodeTyper(pn.viewable.Viewer):
    value = param.String()
    title = param.String()
    command = param.String(default=COMMAND)
    language = param.String(default="python")
    theme=param.String(default="tomorrow_night")
    period= param.Integer(default=25)
    height=param.Integer(650)
    accent_base_color=param.Color(ACCENT_BASE_COLOR)

    def __init__(self, **params):
        if "value" in params and isinstance(params["value"], pathlib.Path):
            params["value"]=params["value"].read_text()

        super().__init__(**params)

        raw_css = f"""
body {{
    background: {self.accent_base_color};
    margin: 0px;
    min-height: 100vh;
}}
"""
        self._style = pn.pane.HTML("<style>" + raw_css + "</style>", height=0, width=0, margin=0)
        self._ace = pn.widgets.Ace(language=self.language, theme=self.theme, height=self.height, margin=0)
        self._terminal = pn.pane.Markdown("$ ", margin=(0,25), background="#25282c", style={"color": "white"}, height=75)
        self._layout = pn.Column(
            pn.Column(
                self._style,
                pn.pane.Markdown(self.title, style={"color": "white"}),
                pn.Row(pn.pane.SVG(SVG, margin=7), pn.Spacer(), background="#25282c", height=30, margin=0),
                pn.pane.Markdown("&nbsp; &nbsp; `script.py`", background="#25282c", margin=0, style={"color": "white"}),
                self._ace,
                pn.Row(pn.Spacer()),
                pn.Column(self._terminal,background="#25282c", margin=0),
                margin=(50, 150),
            ),
            background=ACCENT_BASE_COLOR,
        )

        chars = list(self.value)
        command = list(self.command)
        values = {"ace_value": "", "terminal_value": ""}
        def typer():
            if chars:
                char = chars.pop(0)
                self._ace.value = values["ace_value"] = values["ace_value"] + char
            elif command:
                char = command.pop(0)
                self._terminal.object = values["terminal_value"] = values["terminal_value"] + char

        pn.state.onload(lambda: pn.state.add_periodic_callback(typer, period=self.period))

    def __panel__(self):
        return self._layout