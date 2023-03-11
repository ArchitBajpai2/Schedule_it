import spacy
from flask import Flask, request, jsonify

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

@app.route('/schedule', methods=['POST'])
def schedule():
    text = request.json['text']
    doc = nlp(text)

    participants = []
    date = None
    time = None
    agenda = None
    duration = None

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            participants.append(ent.text)
        elif ent.label_ == "DATE":
            date = ent.text
        elif ent.label_ == "TIME":
            time = ent.text
        elif ent.label_ == "EVENT":
            agenda = ent.text
        elif ent.label_ == "DURATION":
            duration = ent.text

    response = {
        "participants": participants,
        "date": date,
        "time": time,
        "agenda": agenda,
        "duration": duration
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)