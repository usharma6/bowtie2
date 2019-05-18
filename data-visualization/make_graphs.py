from parser import parse
import plotly.plotly as py
import plotly
import plotly.graph_objs as go

def matched_vs_unmatched_pie_chart(forward_reads, reverse_reads, unmatched_reads):
    match_chart_labels = ['Forward Reads(Matched)', 'Reverse Reads (Matched)', 'Unmatched Reads']
    match_chart_values = [forward_reads, reverse_reads, unmatched_reads]
    return (match_chart_labels, match_chart_values)

def phred33_to_q(qual):
  #Turn Phred+33 ASCII-encoded quality into Phred-scaled integer
  return ord(qual)-33

def q_to_p(Q):
  #Turn Phred-scaled integer into error probability
  return 10.0 ** (-0.1 * Q)

def read_quality_converter(read_quality):
    for i in range(len(read_quality)):
        for j in range(len(read_quality[i])):
            #Converting the read quality data to probabilities
            read_quality[i][j] = 100 - int(100 * q_to_p(phred33_to_q(read_quality[i][j])))

def read_quality_box_plot(read_quality):
    data = []
    for i in range(10):
        temp = []
        for j in range(len(read_quality)//10):
            temp += read_quality[(i * 10) + j]
        print(len(temp))
        trace = go.Box(
            y = temp,
            name = str((len(read_quality)//10) * i) + ' - ' + str((len(read_quality)//10) * (i + 1) - 1),
            marker = dict(
                color = 'rgb(0, 128, 128)'
            )
        )
        data.append(trace)
    return data
