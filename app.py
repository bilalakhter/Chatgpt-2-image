from flask import Flask,request,render_template,redirect,url_for


app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        global questiona
        questiona = request.form['query']

        return redirect(url_for('output'))
    else:
        return render_template('index.html')

@app.route('/output')

def output():
    import openai

    # Load your API key from an environment variable or secret management service
    openai.api_key = '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'

    responsi = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = questiona,
        max_tokens =1000,
    )
    resp = responsi.choices[0]['text']

    return render_template("output.html",outresp = resp,yourquestion=questiona)


if __name__ == '__main__':
    app.run()
