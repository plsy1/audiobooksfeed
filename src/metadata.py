import xml.etree.ElementTree as ET
import os, re
import socket

def get_preferred_ip_address():
    try:
        # 尝试使用本地回环地址
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
        s.close()

        return ip_address
    except Exception as e:
        print(f"Error: {e}")

    try:
        # 尝试获取自动分配的IP地址（使用DHCP）
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except Exception as e:
        print(f"Error: {e}")

    # 如果以上两种方式都不可用，选择一个私有IP地址范围
    return '192.168.1.1'  # 你可以根据需要更改此值

def get_metadata(abs_file_path):
    metadata = {}
    chapters = []

    with open(abs_file_path, "r", encoding="utf-8") as abs_file:
        # 读取前18行
        lines = [next(abs_file).strip() for _ in range(18)]

        # 处理键值对
        for line in lines:
            parts = line.split("=")
            if len(parts) == 2:
                key, value = parts
                metadata[key.strip()] = value.strip()

        # 处理章节信息
        for line in abs_file:
            if line.startswith("[CHAPTER]"):
                chapter = {}
                for _ in range(3):
                    key, value = next(abs_file).strip().split("=")
                    chapter[key.strip()] = value.strip()
                chapters.append(chapter)

    metadata["chapters"] = chapters
    return metadata
def get_reader(abs_file_path):
    reader = ''
    with open(abs_file_path, "r", encoding="utf-8") as abs_file:
        reader = abs_file.readline().strip()

    return reader

def get_desc(abs_file_path):
    desc = ''
    with open(abs_file_path, "r", encoding="utf-8") as abs_file:
        desc = abs_file.read()

    return desc


def get_file_names(directory):
    files = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".m4a"):
            files.append(filename)
    return files


def get_all_folders(dir):
    # 获取当前工作目录


    # 使用 os.listdir 获取当前目录下的所有文件和文件夹
    all_items = os.listdir(dir)

    # 使用列表推导式筛选出文件夹
    folders = [item for item in all_items if os.path.isdir(os.path.join(dir, item))]

    return folders

def sanitize_filename(title):
    # 使用正则表达式过滤掉非字母、数字、下划线、连字符和空格的字符
    sanitized_title = re.sub(r'[^\w\s-]', '', title)
    
    # 替换空格和连字符为下划线
    sanitized_title = re.sub(r'[-\s]+', '_', sanitized_title)
    
    return sanitized_title