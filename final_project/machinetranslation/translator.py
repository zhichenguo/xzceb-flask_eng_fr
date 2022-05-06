"""
This module includes two funtions for English and French translators between each other.
"""

import json
import os

from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = "2018-05-01"

def english_to_french(english_text):
    """
    This function handles translating English string to French string.
    """

    if english_text is None or english_text == "":
        return ""

    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version=VERSION,
        authenticator=authenticator
    )

    language_translator.set_service_url(URL)

    try:
        # Invoke a method
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()

        french_text = translation["translations"][0]["translation"]

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        french_text = "N/A"

    return french_text

def french_to_english(french_text):
    """
    This function handles translating French string to English string.
    """

    if french_text is None or french_text == "":
        return ""

    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version=VERSION,
        authenticator=authenticator
    )

    language_translator.set_service_url(URL)

    try:
        # Invoke a method
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()

        english_text = translation["translations"][0]["translation"]

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        english_text = "N/A"

    return english_text
