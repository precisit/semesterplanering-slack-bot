import logging
logging.basicConfig(level=logging.DEBUG)
import os
from slack import WebClient
from slack.errors import SlackApiError
import datetime
import calendar

slack_token = os.environ.get('SLACK_BOT_TOKEN')
slack_client = WebClient(slack_token, ssl=True)


if __name__ == "__main__":
    dt = datetime.datetime.today()
    current_month = calendar.month_name[dt.month]
    semester_planning_month = calendar.month_name[(dt.month+3) % 12]
    try:
      response = slack_client.chat_postMessage(
        channel="semesterplanerings-bot",
        text="Hej! Nu i {} är det dags att söka semester för {} blablabla :sunglasses: :sunny:".format(current_month, semester_planning_month)
      )
    except SlackApiError as e:
      # You will get a SlackApiError if "ok" is False
      assert e.response["error"]