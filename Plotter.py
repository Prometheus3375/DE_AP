from plotly.graph_objs import Scatter as Curve
from plotly.offline import plot


def Plot(xlist: list, ylists: tuple, names: tuple, plotname: str, x_asympt=None, y_asympt=None):
    graphs = []
    asympt = not (x_asympt is None or y_asympt is None)
    for l in range(len(ylists)):
        graphs.append(Curve(
            x=xlist,
            y=ylists[l],
            mode="lines",
            name=names[l],
            connectgaps=False
        ))
        if asympt:
            graphs.append(Curve(
                x=x_asympt,
                y=y_asympt[l],
                mode="lines",
                name="Asymptotes for " + names[l],
                connectgaps=False,
                line=dict(
                    color="rgb(204, 204, 204)",
                    dash="dash")
            ))
    fig = dict(data=graphs, layout=dict(title=plotname))
    plot(fig, filename="plots\\" + plotname + ".html")
