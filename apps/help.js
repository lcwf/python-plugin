import plugin from '../../../lib/plugins/plugin.js'
import fs from 'node:fs'
import lodash from "lodash";
import { segment } from "oicq";
import Common from "../model/Common.js";
import exepy from "../model/exepy.js"
//项目路径
const _path = process.cwd();
let elems=['cryo','electro','geo','hydro','pyro','anemo']
export class help extends plugin {
  constructor (e) {
    super({
      name: 'py菜单',
      dsc: 'py功能那个列表',
      event: 'message',
      priority: 270,
      rule: [
        {
          reg: "#?py(菜单|命令|帮助|help|说明|功能|指令|使用说明)$", //匹配消息正则，命令正则
          fnc: 'help',
          des:"【#py菜单】获取py拥有的功能"
        }
      ]
    })
    this.exepy=new exepy(e)
  }
  
  
  async help() {
    let e=this.e
    if (!/py/.test(e.msg)) {
      return false;
    }
    //logger.info(this.name)
    let help_list=[{
      group:"命令",
      list:[]
    }]
    
    for (var key of this.exepy.plugins['priority']){
      if (key['key']=='python-plugin'){
        let func=key['class']
        let fun=new func()        
        for (var i of fun.rule){
          let list={}
          let lists=i.des.split('】')
          list['icon']=parseInt(lodash.random(0,94))
          list['title']=lists[0].replace('【','')
          list['desc']=lists[1]
          help_list[0].list.push(list)
        }
      }
    }
    
  //let helpFile = {};
  //helpFile = await import(`file://${helpFilePath}?version=${new Date().getTime()}`);

  //const { helpCfg } = helpFile;
  //console.log(helpCfg)
  let helpGroup = [];

  lodash.forEach(help_list, (group) => {
    if (group.auth && group.auth === "master" && !e.isMaster) {
      return;
    }

    lodash.forEach(group.list, (help) => {
      let icon = help.icon * 1;
      if (!icon) {
        help.css = `display:none`;
      } else {
        let x = (icon - 1) % 10, y = (icon - x - 1) / 10;
        help.css = `background-position:-${x * 50}px -${y * 50}px`;
      }

    });

    helpGroup.push(group);
  });
  let elem1=lodash.random(0,elems.length-1)
  await this.reply(await Common.render("help/index", {
    helpCfg: helpGroup,
    element: elems[elem1]
  }, { e,  scale: 1.2 }))
}
}