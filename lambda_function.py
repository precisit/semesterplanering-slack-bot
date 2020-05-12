import logging
logging.basicConfig(level=logging.DEBUG)
import os
from slack import WebClient
from slack.errors import SlackApiError
import datetime
import json


calendar_sv = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december']
slack_token = os.environ.get('SLACK_BOT_TOKEN')
slack_client = WebClient(slack_token, ssl=True)


def send_reminder():
    dt = datetime.datetime.today()
    current_month = calendar_sv[dt.month-1]
    semester_planning_month = calendar_sv[(dt.month+3-1) % 11]
    try:
        response = slack_client.chat_postMessage(
            channel="semesterplanerings-bot",
            text="Hej! Nu i {} är det dags att söka semester för {} :sunglasses: :sunny:".format(current_month, semester_planning_month)
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]


def lambda_handler(event, context):
    send_reminder()
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

