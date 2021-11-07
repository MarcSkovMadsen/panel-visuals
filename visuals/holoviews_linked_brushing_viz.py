from base import CodeTyper, SNIPPETS_ROOT, COMMAND
import panel as pn

pn.extension(sizing_mode="stretch_width")

CodeTyper(
    title="# Cross Filtering with hvPlot, Holoviews and PANEL",
    value=SNIPPETS_ROOT/"holoviews_linked_brushing_app.py",
    command="$ pip install panel holoviews hvplot shapely\n" + COMMAND,
    accent_base_color="#ff286e"
).servable()