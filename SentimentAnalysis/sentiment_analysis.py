"""
This module provides a simple Flask web application and a function
for sentiment analysis using the Watson NLP service.
"""
import requests

def sentiment_analyzer(text_to_analyze):
    """
    This function analyzes a string and sends it to Watson to get the sentiment analysis of it.
    """
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        # Set a timeout of 10 seconds
        response.raise_for_status()  # Raises an HTTPError for bad responses
        formatted_response = response.json()

        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        else:
            label = None
            score = None
    except requests.exceptions.RequestException as e:
        return {'error': str(e), 'label': None, 'score': None}

    return {'label': label, 'score': score}

    #run python python3.11
    # in python shell: from sentiment_analysis import sentiment_analyzer
    #import json
    #from sentiment_analysis import sentiment_analyzer
    #response = sentiment_analyzer("I love this new technology")
    #formatted_response = json.loads(response)
    #print(formatted_response)

