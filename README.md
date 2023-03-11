# Schedule_it
Overview-
This API is used to extract information related to scheduling a meeting from a given text input. The API is built using the Python Flask framework and uses the spaCy NLP library to perform entity recognition on the input text.

Endpoint-
The API exposes a single endpoint /schedule that accepts POST requests.

Inputs-
The /schedule endpoint expects a JSON payload containing a text key with the input text to be processed. The input text should be a string describing the details of the meeting to be scheduled.

Example Input-
json
Copy code
{
    "text": "Can we schedule a meeting with John and Jane on Monday at 2pm to discuss the project proposal? It shouldn't take more than an hour."
}
Outputs
The /schedule endpoint returns a JSON payload containing the extracted information related to the meeting schedule. The payload contains the following keys:

participants: A list of the names of the participants in the meeting.
date: The date of the meeting in string format.
time: The time of the meeting in string format.
agenda: The agenda of the meeting in string format.
duration: The duration of the meeting in string format.
If any of the above keys cannot be extracted from the input text, the value will be null.

Example Output-
json
{
    "participants": ["John", "Jane"],
    "date": "Monday",
    "time": "2pm",
    "agenda": "discuss the project proposal",
    "duration": "an hour"
}

Example Usage-
Here is an example of how to use the API using the Python requests library:

python-
import requests

url = "http://localhost:5000/schedule"
payload = {
    "text": "Can we schedule a meeting with John and Jane on Monday at 2pm to discuss the project proposal? It shouldn't take more than an hour."
}

response = requests.post(url, json=payload)

print(response.json())
The output of the above code should be:

json-
{
    "participants": ["John", "Jane"],
    "date": "Monday",
    "time": "2pm",
    "agenda": "discuss the project proposal",
    "duration": "an hour"
}
