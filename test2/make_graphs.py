from parser import parse
import plotly.plotly as py
import plotly.graph_objs as go
forward_reads, reverse_reads, unmatched_reads, read_quality, match_scores = parse()

match_chart = pygal.Pie()
match_chart.add('Forward Reads(Matched)', forward_reads)
match_chart.add('Reverse Reads(Matched)', reverse_reads)
match_chart.add('Unmatched Reads', unmatched_reads)
read_qulity_chart =
