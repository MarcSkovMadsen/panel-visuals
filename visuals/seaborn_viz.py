from base import CodeTyper, SNIPPETS_ROOT
import panel as pn

pn.extension(sizing_mode="stretch_width")

CodeTyper(
    title="# Make Seaborn Interactive with PANEL",
    value=SNIPPETS_ROOT/"seaborn_app.py",
    accent_base_color="#6082A2"
).servable()