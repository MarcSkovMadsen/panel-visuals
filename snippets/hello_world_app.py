import panel as pn

pn.extension(sizing_mode="stretch_width")

pn.template.FastListTemplate(
    site="Panel",
    title="Hello Header",
    sidebar=["# Sidebar"],
    main=["# Main"],
    header_background="#FFB3D9"
).servable()