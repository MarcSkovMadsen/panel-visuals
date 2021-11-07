import hvplot.pandas
import holoviews as hv
import panel as pn
from bokeh.sampledata.iris import flowers

pn.extension(sizing_mode="stretch_width")
hv.extension("bokeh")

accent_color = "#ff286e"

scatter = flowers.hvplot.scatter(
    x="sepal_length", y="sepal_width", c=accent_color, responsive=True, height=420
)
hist = flowers.hvplot.hist("petal_width", c=accent_color, responsive=True, height=420)

scatter.opts(size=10)

selection_linker = hv.selection.link_selections.instance()

scatter = selection_linker(scatter)
hist = selection_linker(hist)

scatter.opts(tools=["hover"], active_tools=["box_select"])
hist.opts(tools=["hover"], active_tools=["box_select"])

pn.template.FastListTemplate(
    site="Panel",
    title="Cross Filtering",
    header_background=accent_color,
    main=[scatter, hist],
).servable()