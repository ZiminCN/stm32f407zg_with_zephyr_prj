import os
import dotenv
import datetime
dotenv_file = dotenv.find_dotenv('VERSION')
dotenv.load_dotenv(dotenv_file)

VERSION_MINOR = int(os.environ['VERSION_MINOR'])
os.environ['VERSION_MINOR'] = str(VERSION_MINOR +1)
os.environ['BUILD_DATE']=datetime.datetime.now().strftime("%Y%m%d")

dotenv.set_key(dotenv_file, "VERSION_MINOR", os.environ["VERSION_MINOR"])
dotenv.set_key(dotenv_file, "BUILD_DATE", os.environ["BUILD_DATE"])
