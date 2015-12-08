from flask import Flask, jsonify
from flask import make_response
from flask import request
from reportlab.pdfgen import canvas

import requests, json

app = Flask(__name__)

elections = [
        {

            "id":"BDE",
            "votes":
            [
                {
                    "choix":1,
                    "prenom":"JP"
                }
            ]
        }
]

@app.route('/Elections', methods=['GET'])
def api_elections():
    return jsonify({'elections':elections})

@app.route('/Elections/<electionId>', methods=['GET'])
def api_election(electionId):
    election = [election for election in elections if election['id']== electionId]
    if len(election) == 0:
        abort(404)
    return jsonify({'election':election[0]})



if __name__ == '__main__':
    app.run(host='0.0.0.0')
