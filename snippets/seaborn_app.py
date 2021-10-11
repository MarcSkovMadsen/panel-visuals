import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")

def apply_theme(theme="theme"):
    if theme == "dark":
        sns.set_style("darkgrid")
        plt.style.use("dark_background")
    else:
        plt.style.use("default")
        sns.set_style("whitegrid")

def plot(input="#6082A2", theme="default"):
    apply_theme(theme=theme)

    fig0 = sns.displot(penguins, x="flipper_length_mm", color=input, legend=False).fig
    fig0.set_size_inches(14, 8)
    return fig0

import panel as pn

pn.extension(sizing_mode="stretch_width")

THEME = str(pn.state.session_args.get("theme", [b"default"])[0].decode("utf8"))
select = pn.widgets.ColorPicker(value="#6082A2", name="Color")
interactive_plot=pn.bind(plot, input=select, theme=THEME)
pn.template.FastListTemplate(
    site="Panel", title="Works With The Tools You Know And Love",
    main=[pn.panel(interactive_plot, sizing_mode="stretch_both"), select],
    header_background="#6082A2", accent_base_color="#6082A2"
).servable()
