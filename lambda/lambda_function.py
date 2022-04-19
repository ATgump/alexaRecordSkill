
import logging
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Launches the Skill
class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return (
            handler_input.response_builder
                .set_should_end_session(False)
                .response
        )

#Records the TESS files
class TESSIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("TESSIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response 
        return handler_input.response_builder.set_should_end_session(True).response

#Records the RADVESS files
class RADVESSIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("RADVESSIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response 
        return handler_input.response_builder.set_should_end_session(True).response

#Add the Skill Intent Handlers to SkillBuilder
sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TESSIntentHandler())
sb.add_request_handler(RADVESSIntentHandler())
lambda_handler = sb.lambda_handler()