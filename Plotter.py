from plotly.graph_objs import Scatter as Curve
from plotly.offline import plot


def Plot(xlist: list, ylists: tuple, names: tuple, colors: tuple, plotname: str):
    graphs = []
    L = len(ylists)
    for l in range(L):
        graphs.append(Curve(
            x=xlist,
            y=ylists[l],
            mode="lines",
            name=names[l],
            connectgaps=False,
            line=dict(color=colors[l]),
            legendgroup=names[l]
        ))
    fig = dict(data=graphs, layout=dict(title=plotname))
    plot(fig, filename="plots\\" + plotname + ".html")
