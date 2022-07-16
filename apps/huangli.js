import plugin from '../../../lib/plugins/plugin.js'
import fs from 'node:fs'
import { segment } from "oicq";
import {createRequire} from "module";
import exepy from "../model/exepy.js"
const require = createRequire(import.meta.url);
//项目路径
const _path = process.cwd();
export class huangli extends plugin {
  constructor (e) {
    super({
      name: '在哪里功能',
      dsc: '查询资源等',
      event: 'message',
      priority: 270,
      rule: [
        {
          reg: "^#.*(在哪|在哪里|哪有|哪里有)|(在哪里菜单)$", //匹配消息正则，命令正则
          fnc: 'cailiao'
        }
      ]
    })
    this.exepy=new exepy(e)
  }
  
  
  async cailiao() {
    if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
      let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
      if(cfg['在哪里']=='关闭'){return false;}
    }
    
    let msg1 =this.e.msg.replace(/#|在|哪|里|有|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
    let n= msg1.match('渊下宫')?7:msg1.match('层岩')?9:(msg1.match('海岛')||msg1.match('金苹果'))?12:2;
    let msg2=(n==7)?msg1.replace(/渊下宫/,''):(n==12)?msg1.replace(/海岛/,'').replace(/金苹果/,''):msg1.replace(/层岩/,'')
    if (this.e.msg.match('菜单')) msg2='菜单';
    let command = "python ./plugins/python-plugin/py/qrps.py "+msg2+' '+n;
    let stdout =await this.exepy.exepy(command).catch(err=>{
      logger.info(err)
      return false})
    logger.info(stdout)
    if (stdout?.trim()=="error"){
      return false
    }else{
      let msg = [
              //stdout,
              segment.image(`file:///${_path}/plugins/python-plugin/resrouces/cailiaodian/${msg2}.jpg`)
              ]
      await this.reply(msg)
    }
  }
}