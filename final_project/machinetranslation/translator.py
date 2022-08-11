"""
This module contains functions to translate text from different languages
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-11',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    This function translate from english to french

    Args:
        english_text (_type_): english text to translate

    Returns:
        _type_: translated text
    """
    # write the code here
    french_text = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']


def french_to_english(french_text):
    """
    This function translate from french to english

    Args:
        french_text (_type_): french text to translate

    Returns:
        _type_: translated text
    """
    # write the code here
    english_text = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
