# audiobooksfeed
本地有声书RSS订阅链接生成，可用于Apple Podcast

可识别的文件结构如下：

├── 有声书文件夹 1
│   ├── EP01.m4a
│   ├── EP02.m4a
│   ├── cover.jpg
│   ├── desc.txt
│   ├── metadata.abs
│   └── reader.txt
├── 有声书文件夹 2
│   ├── EP01.m4a
│   ├── EP02.m4a
│   ├── cover.jpg
│   ├── desc.txt
│   ├── metadata.abs
│   ├── podcast.xml
│   └── reader.txt

## 配置

1. 克隆本项目

```sh
git clone https://github.com/plsy1/audiobooksfeed
```

2. 修改`config.ini`

```
[Server]
PORT = 8888 						## 文件服务器端口号
DIRECTORY = /audio 			## 有声书根目录
```

3. 运行`main.py`

## 其他

生成的RSS XML文件存储在有声书根目录下

RSS链接文件存储在main.py同目录下

