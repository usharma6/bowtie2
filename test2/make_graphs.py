from parser import parse
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
forward_reads, reverse_reads, unmatched_reads, read_quality, match_scores = parse()

def matched_vs_unmatched_pie_chart():
    match_chart_labels = ['Forward Reads(Matched)', 'Reverse Reads (Matched)', 'Unmatched Reads']
    match_chart_values = [forward_reads, reverse_reads, unmatched_reads]
    return (match_chart_labels, match_chart_values)

def phred33_to_q(qual):
  #Turn Phred+33 ASCII-encoded quality into Phred-scaled integer
  return ord(qual)-33

def q_to_p(Q):
  #Turn Phred-scaled integer into error probability
  return 10.0 ** (-0.1 * Q)

def read_quality_converter():
    for i in range(len(read_quality)):
        for j in range(len(read_quality[i])):
            #Converting the read quality data to probabilities
            read_quality[i][j] = int(100 * q_to_p(phred33_to_q(read_quality[i][j])))

def read_quality_box_plot():
    data = []
    for i in range(len(read_quality)):
        trace = go.Box(
            y = read_quality[i],
            name = str(i),
            marker = dict(
                color = 'rgb(0, 128, 128)'
            )
        )
        data.append(trace)
    return data

read_quality_converter()
labels, values = matched_vs_unmatched_pie_chart()
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

data = read_quality_box_plot()

layout = go.Layout(
    title = "Read Quality Scores by Location"
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig)
