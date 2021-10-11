from base import CodeTyper, SNIPPETS_ROOT
import panel as pn

pn.extension(sizing_mode="stretch_width")

CodeTyper(
    title="# Hello World Panel App",
    value=SNIPPETS_ROOT/"hello_world_app.py",
    accent_base_color="#FFB3D9",
    height=250,
).servable()