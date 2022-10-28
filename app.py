
from flask import  Flask, render_template
import pandas as pd
app = Flask(__name__)
df = pd.read_csv('price.csv')
df.to_csv('price.csv', index=None)


@app.route('/')
@app.route('/table')
def table():
    data = pd.read_csv('price.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
