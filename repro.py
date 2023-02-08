import time
import whylogs as y 
import logging
import pandas as pd
from whylogs.api.logger import TimedRollingLogger

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

df = pd.read_csv('data/really-short.csv')


logger: TimedRollingLogger = y.logger(mode="rolling", interval=5, when="M", base_name="profile_")
logger.append_writer('whylabs', org_id="org-JpsdM6", api_key="RBzREc0IuL.ZCuVOPhn30HJ1XqYbJSHJwpwS3GEDj0YB0rAgfV8cQ5CXzpgibTo9", dataset_id='model-14')

logger.log(df)
logger._do_rollover()
time.sleep(1)
logger._do_rollover()

