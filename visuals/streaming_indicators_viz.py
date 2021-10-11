from base import CodeTyper, SNIPPETS_ROOT
import panel as pn

pn.extension(sizing_mode="stretch_width")

CodeTyper(
    title="# Make Streaming Dashboards with PANEL",
    value=SNIPPETS_ROOT/"streaming_indicators_app.py",
    accent_base_color="#428bca"
).servable()