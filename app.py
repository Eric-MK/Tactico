from flask import Flask, request, jsonify
import pandas as pd   # <---- Add this line

import app2  # Assuming that 'app2' is the name of your existing script without the '.py' extension

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    player_type = request.json['player_type']
    query = request.json['query']
    count = request.json['count']
    comparison = request.json['comparison']
    league = request.json['league']

    try:
        result = app2.getRecommendations(player_type, query, count, comparison, league)

        # Check if the result is a DataFrame and convert to dict if necessary
        if isinstance(result, pd.DataFrame):
            result = result.to_dict(orient='records')
            
        # Return the result (which should now definitely be a dictionary)
        return jsonify(result)

    except ValueError as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
    app.run(debug=True)
