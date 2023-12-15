from src.conf import ConfigManager
from src.metadata import get_preferred_ip_address
from src.database import *

config = ConfigManager()
config.server_host = get_preferred_ip_address()
initialize_database()



