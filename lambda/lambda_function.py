# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
from email.mime import audio
from http.client import ResponseNotReady, responses
import logging
import ask_sdk_core.utils as ask_utils
import re

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.services.api_client_request import ApiClientRequest
from ask_sdk_model import Response
from ask_sdk_model.interfaces.audioplayer import AudioItem, Stream, PlayDirective, PlayBehavior
from utils import create_presigned_url
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Your recorder is open"
        return (
            handler_input.response_builder
                .set_should_end_session(False)
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class RecordIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RecordIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output =  "Record"
        audio_url = create_presigned_url("Media/testSmallSilence.mp3")
        audio_url= re.sub('&','&amp;',audio_url)
        reprompt_output = "<audio src=\""+audio_url+"\"/>"
        return (
            handler_input.response_builder
                .speak(reprompt_output)
                .set_should_end_session(False)
                .ask("")
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
class StopRecordIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("StopRecordIntent")(handler_input)
    def handle(self,handler_input):
        return(
            handler_input.response_builder
            .set_should_end_session(True)
            .response
        )




        

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(RecordIntentHandler())
sb.add_request_handler(StopRecordIntentHandler())
lambda_handler = sb.lambda_handler()