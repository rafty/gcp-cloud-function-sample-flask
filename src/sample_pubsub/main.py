import base64
import pprint as pp

from flask import current_app


def sample_pubsub(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """

    data = base64.b64decode(event['data']).decode('utf-8')

    current_app.logger.info(
        f'This Function was triggered by messageId {context.event_id} published at {context.timestamp}: \n'
        f'decoded_data: "{data}" \n'
        f'event: {pp.pformat(event, indent=2)} \n'
        f'context: {context}'
    )