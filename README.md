# audiobooksfeed
本地有声书RSS订阅链接生成，可用于Apple Podcast 

![效果](https://github.com/plsy1/audiobooksfeed/blob/main/img/podcast.png?raw=true)

结果保存到html文件中，手动添加到podcast即可。

![](https://github.com/plsy1/audiobooksfeed/blob/main/img/result.png?raw=true)

可识别的文件结构如下：

![](https://github.com/plsy1/audiobooksfeed/blob/main/img/tree.png?raw=true)

## Features

- 支持audiobookshelf metadata刮削
- 支持红叶有声书刮削
- 生成 RSS 订阅链接

## Usage

1. 克隆本项目

```sh
git clone https://github.com/plsy1/audiobooksfeed
```

2. 修改`config.ini`带注释的部分

```ini
[Server]
PORT = 1818 #文件服务器端口号
DIRECTORY = /audiobooks #有声书根目录
AUDIO_EXTENSIONS = .m4a, .mp3

[DATABASE]
FILENAME = data.db
```



