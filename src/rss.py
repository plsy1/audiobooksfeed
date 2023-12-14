import xml.etree.ElementTree as ET
from . import config
from urllib.parse import quote
import os, time
from src.metadata import *


def generate_item_element(host,bookdir, file_name,reader):
    
    
    encoded_file_name = quote(file_name, safe="")
    
    base_name, file_extension = os.path.splitext(file_name)
    
    # 创建 <item> 元素
    item = ET.Element("item")

    # 添加 <title> 元素到订阅项，使用文件名
    item_title = ET.SubElement(item, "title")
    item_title.text = base_name
    
    item_author = ET.SubElement(item, "itunes:author")
    item_author.text = reader if reader else "Default Author Name"
    
    # 添加 <enclosure> 元素到订阅项
    enclosure = ET.SubElement(item, "enclosure", attrib={
        "url": f"{host}/{bookdir}/{encoded_file_name}",
        "type": ("audio/x-m4a")
    })


    return item


def generate_podcast_feed(metadata, reader,desc,episode_list,book_dir,timestamp):
    
    encoded_book_dir = quote(book_dir, safe="")
    
    # 创建根元素 <rss>
    rss = ET.Element("rss", version="2.0", attrib={
        "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "xmlns:content": "http://purl.org/rss/1.0/modules/content/"
    })

    # 创建子元素 <channel>
    channel = ET.SubElement(rss, "channel")

    # 添加 <title> 元素
    title = ET.SubElement(channel, "title")
    title.text = metadata.get("title", "Your Podcast Title")

    # 添加 <link> 元素
    link = ET.SubElement(channel, "link")
    link.text = metadata.get("website", "http://www.yourpodcastwebsite.com")

    # 添加 <language> 元素
    language = ET.SubElement(channel, "language")
    language.text = metadata.get("language", "en-us")

    # 添加 <itunes:author> 元素
    author = ET.SubElement(channel, "itunes:author")
    author.text = reader if reader else "Default Author Name"

    # 添加 <itunes:summary> 元素
    itunes_summary = ET.SubElement(channel, "itunes:summary")
    itunes_summary.text = desc if desc else "Your podcast description."

    # 添加 <description> 元素
    description = ET.SubElement(channel, "description")
    description.text = desc if desc else "Your podcast description."


    # 添加 <itunes:owner> 元素
    itunes_owner = ET.SubElement(channel, "itunes:owner")
    itunes_owner_name = ET.SubElement(itunes_owner, "itunes:name")
    itunes_owner_name.text = metadata.get("owner_name", "Your Name")
    itunes_owner_email = ET.SubElement(itunes_owner, "itunes:email")
    itunes_owner_email.text = metadata.get("owner_email", "your@email.com")

    # 添加 <itunes:image> 元素
    itunes_image = ET.SubElement(channel, "itunes:image", attrib={"href": metadata.get("cover_image", f'http://{config.host}:{config.server_port}/{encoded_book_dir}/cover.jpg')})

    

    for file_name in episode_list:
        item = generate_item_element(f'http://{config.host}:{config.server_port}',encoded_book_dir,file_name,reader)
        channel.append(item)


    # 将 XML 树转换为字符串
    xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(rss, encoding="utf-8").decode()

    # 将生成的 XML 字符串写入文件
    # filename = sanitize_filename(metadata["title"])
    with open(f"{config.root_folder}/{book_dir}.xml", "w") as xml_file:
        xml_file.write(xml_string)

    print("Podcast feed with metadata generated successfully!")
    output_path = f"rss_{timestamp}.txt"  # 文件名加上时间戳
    with open(output_path, "a") as output_file:
        
        output_file.write(f'文件目录名：{book_dir}\n')
        rss_link = f'http://{config.host}:{config.server_port}/xml/{encoded_book_dir}.xml\n\n'
        output_file.write('RSS链接： ' + rss_link)


def generate_rss_file():
    
    audio_books = get_all_folders(config.root_folder)
    timestamp = int(time.time())
    
    for book_dir in audio_books:
        current_dir = f'{config.root_folder}/{book_dir}'
        print("current dir",current_dir)
        episode_files_name = get_file_names(current_dir)
        
        metadata_path = current_dir + "/metadata.abs"
        metadata = get_metadata(metadata_path)
        
        reader_path = current_dir + "/reader.txt"
        reader = get_reader(reader_path)
        
        desc_path = current_dir + "/desc.txt"
        desc = get_desc(desc_path)
        
        
        generate_podcast_feed(metadata,reader,desc,episode_files_name,book_dir,timestamp)