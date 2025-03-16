exec(open('util.py').read())
from flask import Flask, render_template, request
import post_test  # Import the data file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default data
    filtered_data = data.data

    if request.method == 'POST':
        # Get query parameter from form
        query = request.form.get('query')

        # Filter data based on query (optional)
        if query:
            filtered_data = [item for item in data.data if query.lower() in item['name'].lower()]

    return render_template('index.html', data=filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
