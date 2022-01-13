# SDU_6th_Hackathon_2021
Share our ideas of RC505 in beatbox.
#### 三人行，必有我师焉
- 三个人的代码都分别放在了对应的文件夹
- 以及最后临场挣扎的“组合”界面


#### 已经实现了的功能：
1. 通过按键来进行录音（2 seconds）并生成保存的 wav文件（如果原先存在了，则覆盖对应按键下生成的文件）
2. 可以通过按下 x 来记录需要顺序播放的音频，并且“录制”完音频顺序之后，可以自动播放刚刚所实现的顺序下调用文件，播放音频
3. 主界面下能通过点击相应的“音”来自主DIY想要创造的节奏（虽然这不是最终我们想要的）

#### 待解决的问题：
1. 界面有待优化
2. 存在的问题：暂时没有实现录制声音之后循环播放，并且可以任意时刻 终止/开始 录制的声音
3. pyaudio这个包在windows10下均安装失败了，采用Ubuntu的Linux环境做和测试的
4. 录音还没有做到随录随停（只能在代码里面限制，这里设置为了 2 seconds ）
