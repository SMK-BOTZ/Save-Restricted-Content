import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7566645218:AAESBbzZYtnQDLb18QrSMdZR3-HxKWkrSUY")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://madarazbotz:aemHxtb49hACpjd6@cluster0.ed7e2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
