import panel as pn
import pandas as pd

pn.extension(sizing_mode="stretch_width")

dates = [str(d.date()) for d in pd.date_range("2020-01-01", "2021-09-01", freq="MS")]

discrete_slider = pn.widgets.DiscreteSlider(value=dates[0], options=dates, name="Date")

def my_selection(date):
    return f"My selection is {date}"

my_selection_interactive = pn.bind(my_selection, date=discrete_slider)

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Discrete Dates Slider",
    main=[
        pn.Column(discrete_slider, my_selection_interactive)
    ],
    header_background="#6082A2"
).servable()