'''This module translates from English to French and vice versa'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']


URL = os.environ['url']
print(URL)

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''English to French'''
    translated_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translated_text['translations'][0]['translation']

    return french_text


def french_to_english(french_text):
    ''' French to English '''
    translated_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translated_text['translations'][0]['translation']
    return english_text

