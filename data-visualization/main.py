from parser import parse
from make_graphs import *
import sys
import plotly
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='usharma6', api_key='FOmzA8kcJAEIIBBnRBc2')
plotly.tools.set_config_file(world_readable=False, sharing='secret')

readNumber = sys.argv[1]
readSize = sys.argv[2]
filename = 'eg' + readNumber + '.sam'

forward_reads, reverse_reads, unmatched_reads, read_quality, match_scores = parse(filename, readSize)
labels, values = matched_vs_unmatched_pie_chart(forward_reads, reverse_reads, unmatched_reads)
read_quality_converter(read_quality)
box_and_whisker_data = read_quality_box_plot(read_quality)
histogram = go.Histogram(x = match_scores, name = "Match Score", xbins=dict(start=-12,end=0))
pie = go.Pie(labels = labels, values = values, name = "Matched vs. Unmatched")

plotly.offline.plot({
    "data" : [go.Pie(labels = labels, values = values)],
    "layout": go.Layout(title = "Matched vs. Unmatched")
})

plotly.offline.plot({
    "data" : [go.Histogram(x = match_scores, name = "Match Score", xbins=dict(
        start=-12,
        end=0))],
    "layout": go.Layout(title = "Match Scores")
})

layout = go.Layout(
    title = "Read Quality Scores by Location (Percent Change of Accuracy)"
)
fig = go.Figure(data=box_and_whisker_data, layout=layout)
plotly.offline.plot(fig)
