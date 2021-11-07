from base import CodeTyper, SNIPPETS_ROOT
import panel as pn

pn.extension(sizing_mode="stretch_width")

BLUE = "#4099da"

CodeTyper(
    title="# JOIN ORSTED AS A TRADING ANALYST\nA WORLD LEADER IN GREEN ENERGY",
    value=SNIPPETS_ROOT/"trading_analyst_app.md",
    accent_base_color=BLUE,
    command = "$ apply now\n\n",
    language="markdown",
).servable()