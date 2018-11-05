from plotly.graph_objs import Scatter as Curve, Layout
from plotly.offline import plot


ExponentFormat = "SI"


def Plot(xlist: list, ylists: list, names: list, colors: list, plotname: str, xaxis: str, yaxes: str,
         auto_open: bool) -> None:
    graphs = []
    L = len(ylists)
    for l in range(L):
        graphs.append(Curve(
            x=xlist,
            y=ylists[l],
            mode="lines",
            name=names[l],
            connectgaps=False,
            line=dict(color=colors[l])
        ))
    layout = Layout(title="<b>" + plotname + "</b>",
                    titlefont=dict(size=18, color="#333333"),
                    xaxis=dict(
                        title=xaxis,
                        titlefont=dict(size=16, color="#999999"),
                        exponentformat=ExponentFormat,
                        showline=True,
                        zerolinecolor="#aaaaaa",
                        ticklen=5
                    ),
                    yaxis=dict(
                        title=yaxes,
                        titlefont=dict(size=16, color="#999999"),
                        exponentformat=ExponentFormat,
                        showline=True,
                        zerolinecolor="#aaaaaa",
                        ticklen=5,
                        automargin=True,
                        tickprefix="   "
                    )
                    )
    fig = dict(data=graphs, layout=layout)
    plot(fig, filename="plots\\" + plotname + ".html", auto_open=auto_open)
