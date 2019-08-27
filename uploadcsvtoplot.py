from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
import json
import plotly
import plotly.graph_objects as go
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('plotcsv.html')

@app.route('/plotly', methods = ['POST'])
def upload_plotly():
    if request.method == 'POST':
        myf = request.files['file_user']
        fn = secure_filename(myf.filename)

        df = pd.read_csv(fn)
        x = np.array(list(df['x']))
        y = np.array(list(df['y']))
        plot = go.Scatter(x=x, y=y)

        plot = [plot]
        plotJSON = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('grafikplotly.html', x=plotJSON)

@app.route('/matplotlib', methods = ['POST'])
def upload_matplotlib():
    if request.method == 'POST':
        myf = request.files['file_user']
        fn = secure_filename(myf.filename)

        df = pd.read_csv(fn)
        x = np.array(list(df['x']))
        y = np.array(list(df['y']))
        
        plt.plot(x,y, linestyle='-',marker='o', color='red')
        plt.title('Plotting with Matplotlib', fontdict={'fontsize':30})
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.savefig('./static/grafik.png')
        
        return render_template('grafikmatplotlib.html')

if __name__ == '__main__':
    app.run(debug=True)