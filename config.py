"""
This config.py file contains those libraries and methods that need to be run before the
execution of the entrypoint file

Author: Fabio
Date: 14th of Jan
"""
from dotenv import load_dotenv
#load env variables
load_dotenv('config/.env')

import logging 
from dds_internal_tools.logging import logging_helper


# setup logger
logging_helper_obj=logging_helper.LoggingHelper('path/LOGGING_CONFIG.YAML','NAME_LOGGING_FILE')
logger=logging.getLogger('config')

from dds_internal_tools.utils import utils_helper
#get config data dictionary for connecting to sowflake
utils_helper.set_config_data("config/config.yaml")

logger.info('SUCCESS')

