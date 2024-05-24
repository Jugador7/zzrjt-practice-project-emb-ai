from flask import Flask
import requests
import json

def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)  # Set a timeout of 10 seconds
        response.raise_for_status()  # Raises an HTTPError for bad responses
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {'label': label, 'score': score}
    except requests.exceptions.Timeout:
        return "The request timed out."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    
    #run python python3.11

    # in python shell: from sentiment_analysis import sentiment_analyzer

    #import json

    #from sentiment_analysis import sentiment_analyzer
    #response = sentiment_analyzer("I love this new technology")

    #formatted_response = json.loads(response)
    #print(formatted_response)


