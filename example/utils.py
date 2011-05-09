# Import Python logging library
import logging

from django.conf import settings

# Set logger and output level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create the handler
handler = logging.FileHandler(settings.PATH_TO_DEBUG_LOG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
