from base import CodeTyper, SNIPPETS_ROOT
import panel as pn

pn.extension(sizing_mode="stretch_width")

CodeTyper(
    title="# How do I Create a Slider with Discrete Dates?",
    value=SNIPPETS_ROOT/"discrete_dates_slider_app.py",
    accent_base_color="#6082A2",
    height=550,
).servable()