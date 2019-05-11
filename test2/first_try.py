from flask import Flask, render_template, url_for
import pygal
app = Flask(__name__)

f = open("data", "r")
line = f.readline()
totalReads = int(line.split(" ")[0])
line = f.readline()
totalUnpaired = int(line.split(" (")[0])
line = f.readline()
aligned_0 = int(line.split(" (")[0])
line = f.readline()
aligned_1 = int(line.split(" (")[0])
line = f.readline()
aligned_more = int(line.split(" (")[0])
paired_chart = pygal.Pie()
paired_chart.title = 'Paired reads versus Unpaired Reads'
paired_chart.add('Paired', totalReads - totalUnpaired)
paired_chart.add('Unpaired', totalUnpaired)
reads_chart = pygal.Pie()
reads_chart.title = 'Alignment frequency of reads'
reads_chart.add('Aligned 0 times', aligned_0)
reads_chart.add('Aligned 1 time', aligned_1)
reads_chart.add('Aligned >1 times', aligned_more)
paired_chart_data = paired_chart.render_data_uri()
reads_chart_data = reads_chart.render_data_uri()

@app.route("/")
def home():
    return render_template("pie_charts.html", paired_data = paired_chart_data, reads_data = reads_chart_data)

if __name__ == '__main__':
    app.run(debug=True)
