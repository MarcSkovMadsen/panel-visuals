import numpy as np
import pandas as pd
import panel as pn

pn.extension(sizing_mode='stretch_width')

layout = pn.layout.FlexBox(*(
    pn.indicators.Trend(
        data={'x': list(range(10)), 'y': np.random.randn(10).cumsum()},
        width=150,
        height=100,
        plot_type=pn.indicators.Trend.param.plot_type.objects[i%4]
    ) for i in range(28)
))

def stream():
    for trend in layout:
        trend.stream(
            {
                'x': [trend.data['x'][-1]+1],
                'y': [trend.data['y'][-1]+np.random.randn()]
            }, rollover=20)

cb = pn.state.add_periodic_callback(stream, 500)

pn.template.FastListTemplate(
    site="Panel",
    title="Streaming Trend Indicators",
    main=[layout,],
    header_background="#428bca"
).servable()