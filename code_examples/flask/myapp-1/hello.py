"""
My App 1: Hello with Bokeh plot and Jinja2 template.
"""
from bokeh.plotting import figure
from bokeh.embed import components
from flask import Flask, request, render_template, abort, Response

app = Flask(__name__)


@app.route('/')
def hello():
    kwargs = {'title': 'hello'}
    plot = figure(title='circles and lines')
    xdata, ydata = [1, 2, 3], [3, 4, 7]
    plot.circle(xdata, ydata, fill_color='green', size=10, legend='circle')
    plot.line(xdata, ydata, line_dash='dotdash', line_color='red',
              legend='line')
    plot.legend.location = "top_left"
    plot_script, plot_div = components(plot)
    kwargs.update(plot_script=plot_script, plot_div=plot_div)
    if request.method == 'GET':
        return render_template('hello.html', **kwargs)
    abort(404)
    abort(Response('Hello'))


if __name__ == '__main__':
    app.run(debug=True)
