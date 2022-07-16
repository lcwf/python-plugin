# python-plugin适配云崽3.x版本
目前只有在哪里以及表情包功能
其他功能敬请期待

#### 介绍
云崽插件包

#### 安装教程
#机器人搭建教程简述
请自行学习搭建，我只是个总结搬运工，方便群友查看
*写在开头，一定要看
py安装需要一定编程基础，如果连教程都看不懂就趁早放弃吧，别浪费时间了
py搭建过程中遇到的问题，请自行百度，远离CNDS，
如果实在不行可以问群里的大佬，大佬说的也不一定是对的，请带好自己的脑子
还有他人没有义务给你解答问题，也不是谁都缺那点金钱的，别拿金钱来侮辱我们
问问题记得把问题描述详细，提供错误日志，态度诚恳，否则，我只能给你算上一卦了。
网络不是法外之地，请严守道德底线，不传播非法信息，不利用机器人谋取利益。
忠告到此为止，望君好自为之。

1.安装命令，在Yunzai-Bot主目录下运行
`git clone https://gitee.com/linglinglingling-python/python-plugin.git ./plugins/python-plugin/`
需要安装python3.x,3.11是测试版本，不稳定，且和pillow不兼容，不建议使用,推荐使用python3.8

2.linux自带python2.7，需要安装3.8

3.安卓可以通过命令`pkg install python`安装

4.windows前往[python官网](http://www.python.org/downloads/windows/)下载,
[安装教程](http://baijiahao.baidu.com/s?id=1708122987339952711&wfr=spider&for=pc)

5.1python需要配置系统变量，windows安装python时勾选会自动配置
#*注意*windows sever 2012自动添加变量存在问题，需要手动配置，切将python排在最后不带分号
在命令窗口输入`python`
没有报错即可
5.2centos用如下命令配置环境变量，python3换成pip3配置一次
[升级教程](http://zhuanlan.zhihu.com/p/509213626)
目录换成相应目录
`ln -s /usr/local/python3/bin/python3 /usr/bin/python`

6.若果是python2.7，有以下方法
6.1方法一
请将python2.7卸载，安装python3.8
6.2方法二
利用软连接使python指向python3.8，记得先移除原本的软连接，
方法自行百度，保证输出为python3.8即可
这种方法使用pip安装库时需要使用pip3，
或者类似对pip3建立软连接即可
6.3方法三
修改js文件内的调用程序python为python3
这种方法的pip需要使用pip3

7.js需要安装如下库
```
npm install node-schedule
```

8.python需要安装以下库，
打开命令窗口，
如果有python2.x,可能需要将如下命令里的pip替换成pip3
*注意：安装依赖库，需要切换到python-plugin目录下，
requirement.txt里是所需库，版本不强制要求，选择适合自己电脑和python版本的就可以
`pip install -i https://mirrors.aliyun.com/pypi/simple -r requirement.txt`
如果缺少其他库，请自行安装，库名不对的，请自行百度，出现error才是报错，warning可以忽略参考
`pip install 库名 -i https://mirrors.aliyun.com/pypi/simple`
如果安装失败可以换源，将链接换成以下其中之一在此尝试
```
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```
8.安装完后使用`pip list`
即可查看已经安装的python库
有上述库名即成功
有timeout字样，是由于网络原因，重装相应依赖库可
pip install 换成相应包名 -i https://mirrors.aliyun.com/pypi/simple

#### 使用说明
1.更新完后请使用命令：#清理签文
命令列表

```
#黄历
#求签
#解签
签到
#丘丘人别名qq人
#清理签文
#原魔公子
#食物堆高高
#圣遗物磐岩
#丘丘人在哪里
#塔罗牌
#抽取3,19,20,39
顶@12356
表情帮助
#py更新
#订阅up111111111
#订阅番剧111111111
#搜番盾之勇者
#删除订阅111111111
#订阅列表
#原魔菜单
#在哪里菜单
#人生重来
#remake
选择1,2,3
分配1,5,7,6
#py版本
#py设置黄历关闭
#py设置菜单
#推送列表
#推送123455678
```
#新增内容
新增自动监测喵喵云崽和py更新，自动进行更新
新增签到界面，每天和机器人增加好感
新增用户自定义原魔别名
原魔菜单增加别名
新增B站UP主视频动态订阅
Yunzai-Bot插件包，由js调用python实现
新增b站番剧订阅
需要先搜番找到相应id

#免责声明
1.功能仅限内部交流和小范围使用，禁止商用
2.图片素材来源于网络，如有侵权，请联系删除

#其他
[Yunzai-Bot](https://github.com/Le-niao/Yunzai-Bot)
[Miao-Plugun](https://github.com/yoimiya-kokomi/miao-plugin)[gitee](https://gitee.com/yoimiya-kokomi/miao-plugin)
[圣遗物，食物信息](https://www.minigg.cn/)
#我的QQ群：862438532
#Yunzai-Bot QQ群聊:213938015
