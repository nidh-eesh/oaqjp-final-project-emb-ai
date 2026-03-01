import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API
    response = requests.post(url, json = myobj, headers = header)

    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion (highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return formatted output
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores