# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/ZeroTwo/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 14980683  # integer value, dont use ""
    API_HASH = "5bc2e9cd58092119e741c1f2b545c1bf"
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    STRING_SESSION = ""
    OWNER_ID = 5667156680  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "HSSLevii"
    SUPPORT_CHAT = "ZeroTwoMusic"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001745301697
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001793111970
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://yxkxmocj:tTsOkWMZ4hqM_pYbdu8lYPqqnVJVdUeT@heffalump.db.elephantsql.com/yxkxmocj"  # needed for any database modules
    DB_URL = "postgres://owrivopvbczaip:8c24f469ed21a5db5fccd405143072aafb5d902753ef2b6ed5e7395224fc36b1@ec2-18-206-103-49.compute-1.amazonaws.com:5432/da5jikk46tbn3i"
    REDIS_URL = "redis://default:6vsajwd6wq3lNI7T3zMIpltTrU040DJC@redis-19248.c16.us-east-1-3.ec2.cloud.redislabs.com:19248"
    LOAD = []
    MONGO_DB_URI = "mongodb+srv://levi:levi@cluster0.yyyytq2.mongodb.net/?retryWrites=true&w=majority"
    MONGO_DB_URL = "mongodb+srv://levi1:levi1@cluster0.vqyydgr.mongodb.net/?retryWrites=true&w=majority"
    FUNC_DB_URL = "postgres://gfwzjuqb:RCJIaJ3GSJWQ6ZR2rEvsAgtPXHzdx5cL@lucky.db.elephantsql.com/gfwzjuqb"
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    REM_BG_API_KEY = "PxCe5v4ZX3RmoQnPdDzf2TTz"
    SPAMWATCH_API = "QsrtejDpiLrvimOWSQeq6hpLNyMI_RIA_TfKExdSnBKE20I2gIXeDxBxYC76kLE6"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "VQ45LFKYPMJ2LKIU"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "65G8ZKE6050P"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "SOME1HING_privet_990022"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True  # Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
