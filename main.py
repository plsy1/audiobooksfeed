from src.metadata import *
from src.rss import *
from src.server import *
from src import config
import threading

def main():
    
    file_server = FileServer(config.root_folder)
    file_server_thread = threading.Thread(target=file_server.start, args=(config.server_host, int(config.server_port)))
    file_server_thread.start()
    
    gen_new_audio_rss()
    
if __name__ == "__main__":
    main()