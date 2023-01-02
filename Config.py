import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13197673"))
    API_HASH = os.environ.get("API_HASH", "052ce58975f187e3ab08d9fbaa66dfc8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5895789196:AAF_vcdZ5bmRkINIInssPer85bFg0JZveSw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BQANOTEuMTA4LjU2LjEzMAG7Gn8FPLt+lxh9R6HIiQfgqpVce4suPPWC+mPEigBmkPwMm0kQPV1ejLMfrJOMzO8OiaqoG6Od+83UirBHTV/ysTxPtNy1NPfPXfd/eyFkUPsib8Kc7LnzYmn/OzhriJ/DBiV8VPPwcqNGhRwE5aTcjnRYQqjFF4Y+fDRss20/WUb1zoF+erpPBEqCdmfWc425bPKpDfo4wWni+h2oEM3E7Q/RVPDjbYxjxkiCwBUxb342sMfmYqo8tt/ASWf5e8VxqEk8GfqzPWx6N32rBUmY5NQGN0sW8gwrFUoizqpn1GrZpm+0amMTAAWEtGchGWqHcfh1tbXOrG+dKHm9GEyMbw==")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@akkibrossn_bot")
    SUPPORT = os.environ.get("SUPPORT", "2103235088") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "-1001803079661") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5686364473")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
