from src.conf import ConfigManager
from src.metadata import get_preferred_ip_address

config = ConfigManager()
config.host = get_preferred_ip_address()



