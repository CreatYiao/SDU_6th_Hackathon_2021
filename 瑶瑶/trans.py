import os
import subprocess
import sys
import you_get
import moviepy.editor as mp
import ffmpeg

def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()

def trans(in_name, out_name):
    clip = mp.AudioFileClip(in_name)
    clip.write_audiofile(out_name)

if __name__ == '__main__':
    # 视频网站的地址
    # 下载
    # url = 'https://www.bilibili.com/video/BV1YW411v78d/?spm_id_from=333.788.recommend_more_video.2'
    # # 视频输出的位置
    # path = 'Desktop'
    # download(url, path)
    #
    # # 转mp3
    # in_name = r'/home/yee/Desktop/A.flv'
    # out_name = r'/home/yee/Desktop/A.mp3'
    # trans(in_name, out_name)

    # ffmpeg - i / home / yee / Desktop / A.flv - strict - 2 / home / yee / Desktop / output.mp4

    # trans_in_path = "/home/yee/Desktop/B.flv"
    # trans_out_path = "/home/yee/Desktop/B.mp4"
    # subprocess.call(["ffmpeg" ,"-i" ,
    #                  trans_in_path, "-strict", "-2",
    #                  trans_out_path])

    tr = "ffmpeg -i /home/yee/Desktop/B.flv -strict -2 /home/yee/Desktop/outputB.mp4"
    os.system(tr)

