import configparser
import os,sys

class ConfigManager:
    def __init__(self, config_file_path=None):
        if config_file_path is None:
            if getattr(sys, 'frozen', False):  # 检查是否是打包后的运行环境
                binary_dir = os.path.dirname(sys.argv[0])
                config_file_path = os.path.join(binary_dir, 'config.ini')
            else:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                config_file_path = os.path.join(current_dir, 'config.ini')

        self.config = configparser.ConfigParser(inline_comment_prefixes=('#', ';'))
        self.config.read(config_file_path)

        # 获取服务器部分的配置
        self.server_port = self.config['Server']['PORT']
        self.root_folder = self.config['Server']['DIRECTORY']
        #self.host = self.config['Server']['SERVERHOST']
        self.audio_extensions = self.config['Server']['AUDIO_EXTENSIONS']
        
        self.database = self.config['DATABASE']['FILENAME']

