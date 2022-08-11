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


def english_to_french(englishText):
    """
    This function translate from english to french

    Args:
        englishText (_type_): english text to translate

    Returns:
        _type_: translated text
    """
    # write the code here
    frenchText = language_translator.translate(
        text=englishText, model_id='en-fr').get_result()
    return frenchText['translations'][0]['translation']


def french_to_english(frenchText):
    """
    This function translate from french to english

    Args:
        frenchText (_type_): french text to translate

    Returns:
        _type_: translated text
    """
    # write the code here
    englishText = language_translator.translate(
        text=frenchText, model_id='fr-en').get_result()
    return englishText['translations'][0]['translation']
