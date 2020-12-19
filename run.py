from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def form():
    return render_template("form.html")


@app.route('/reccomend', methods=["POST"])
def reccomend():
    """ reccomendページ """
    return render_template('reccomend.html')


# @app.route('/careerplan')
# def reccomend():
#     """ reccomendページ """
#     return render_template('careerplan.html')


if __name__ == '__main__':
    app.run()
