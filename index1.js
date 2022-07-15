import {
  huangli,
  qiuqian,
  jieqian,
  food,
  enemies,
  enemies_name,
  artifacts,  
  cailiao,
  tarot,
  tarot1  
} from "./apps/huangli.js";
import {
  huanying
} from "./apps/huanying.js";
import * as note from "./apps/note.js";
import { 
  rule1,
  examples} from "./apps/examples.js"
import { currentVersion,changelogs } from "./apps/Updatelog.js";
import {
  biaoQing,
  biaoQingHelp
} from "./apps/petpet.js";
import * as readexcel from "./apps/gacha.js";
import Common from "./apps/Common.js";
import {
  bilibilidingyue,
  bilibililist,
  bilibilidelete,
  bilibilisoufan
} from "./apps/bilibili.js";
import * as config from "./config/config.js";
import {
  profileCfg,
  whitelist,
  qingli,
  whitelistdelete,
  python_update
} from "./apps/admin.js";
import {
  life,
  life1,
  life2,
  life3,
  signlist,
  sign
} from "./apps/life.js";
import lodash from "lodash";
export {
  huangli,
  huanying,
  qiuqian,
  jieqian,
  food,
  note,
  enemies,
  enemies_name,
  profileCfg,
  whitelist,
  whitelistdelete,
  bilibililist,
  bilibilidelete,
  bilibilidingyue,
  bilibilisoufan,
  artifacts,
  qingli,
  config,
  sign,
  rule1,
  examples,
  signlist,
  cailiao,
  tarot,
  tarot1,
  biaoQing,  
  life,
  life1,
  life2,
  life3,
  biaoQingHelp,
  python_update
};
let rule = {
  huangli: {
    reg: "^#(黄历|日历)$", //匹配消息正则，命令正则
    describe: "【#黄历|日历】今日迷信", //【命令】功能说明
  },
  profileCfg: {
    reg: "^#?(py|Py|PY)设置(.*)$",
    describe: "【py设置签到开启|关闭】开启关闭py功能",
  },
  huanying: {
    reg: "幻影$",
    describe: "【幻影】隐藏图片",
  },
  whitelistdelete: {
    reg: "^#推送移除(.*)$",
    describe: "【#推送移除+群号】每日60s推送移除群聊，不支持私聊",
  },
  whitelist: {
    reg: "^#推送(.*)$",
    describe: "【#推送+群号】每日60s推送，不支持私聊",
  },
  qiuqian: {
    reg: "^#(求签)$", //匹配消息正则，命令正则

    describe: "【#求签】今日运势", //【命令】功能说明
  },
  jieqian: {
    reg: "^#(解签)$", //匹配消息正则，命令正则

    describe: "【#解签】进行解签", //【命令】功能说明
  },
  sign: {
    reg: "^签到$", //匹配消息正则，命令正则

    describe: "【#签到】进行签到", //【命令】功能说明
  },
  signlist: {
    reg: "^签到排行$", //匹配消息正则，命令正则

    describe: "【签到排行】查看总排行", //【命令】功能说明
  },
  food: {
    reg: "^#(食物).*$", //匹配消息正则，命令正则

    describe: "【#食物堆高高】获取食物信息", //【命令】功能说明
  },
  enemies: {
    reg: "^#(原魔).*$", //匹配消息正则，命令正则

    describe: "【#原魔公子】获取原魔信息", //【命令】功能说明
  },
  enemies_name: {
    reg: "^#.*(别名).*$", //匹配消息正则，命令正则

    describe: "【#丘丘人别名qq人】增加原魔别名", //【命令】功能说明
  },
  artifacts: {
    reg: "^#(圣遗物).*$", //匹配消息正则，命令正则

    describe: "【#圣遗物磐岩】获取圣遗物信息", //【命令】功能说明
  },
  qingli: {
    reg: "^#(清理签文)$", //匹配消息正则，命令正则

    describe: "【#清理签文】清空所有签文", //【命令】功能说明
  },
  cailiao: {
    reg: "^#.*(在哪|在哪里|哪有|哪里有)|(在哪里菜单)$", //匹配消息正则，命令正则

    describe: "【材料名在哪|在哪里|哪有|哪里有】返回一张资源地图", //【命令】功能说明
  },
  tarot: {
    reg: "^#(塔罗牌).*$", //匹配消息正则，命令正则

    describe: "【#塔罗牌】计算今日运势", //【命令】功能说明
  },
  tarot1: {
    reg: "^#(抽取).*$", //匹配消息正则，命令正则

    describe: "【#抽取1,2,3,4】抽取塔罗牌", //【命令】功能说明
  },
  biaoQing: {
    reg: "noCheck", //匹配消息正则，命令正则
    describe: "【爬】头像表情包", //【命令】功能说明
  },
  biaoQingHelp: {
    reg: "^(表情帮助)$", //匹配消息正则，命令正则
    describe: "【表情帮助】头像表情包帮助", //【命令】功能说明
  },
  python_update: {
    reg: "^#(python.*更新)|(py.*更新)$", //匹配消息正则，命令正则
    describe: "【#py|python更新】自动拉取代码", //【命令】功能说明
  },
  bilibililist: {
    reg: "^#订阅列表$", //匹配消息正则，命令正则
    describe: "【#订阅列表】B站订阅列表", //【命令】功能说明
  },
  bilibilisoufan: {
    reg: "^#搜番.*$", //匹配消息正则，命令正则
    describe: "【#搜番+番名】B站番剧id查询", //【命令】功能说明
  },
  bilibilidelete: {
    reg: "^#删除订阅.*$", //匹配消息正则，命令正则
    describe: "【#删除订阅+订阅列表中的uid】删除B站订阅", //【命令】功能说明
  },
  bilibilidingyue: {
    reg: "^#订阅((up|UP)|(番剧|动漫)|(直播)).*$", //匹配消息正则，命令正则
    describe: "【#订阅up|番剧|直播】B站订阅", //【命令】功能说明
  },
  life: {
    reg: "^#人生重来$", //匹配消息正则，命令正则
    describe: "【#人生重来】进行全随机的人生重来", //【命令】功能说明
  },
  life1: {
    reg: "^#remake$", //匹配消息正则，命令正则
    describe: "【#remak】进行全选择的人生重来", //【命令】功能说明
  },
  life2: {
    reg: "^(选择).*$", //匹配消息正则，命令正则
    describe: "【选择1,2,3,4】从十个天赋中选择四个", //【命令】功能说明
  },
  life3: {
    reg: "^(分配).*$", //匹配消息正则，命令正则
    describe: "【分配5,5,5,5】将220点属性分配到四项中", //【命令】功能说明
  },
  help: {
    reg: "^#?py(菜单|命令|帮助|help|说明|功能|指令|使用说明)$",
    describe: "【#py菜单】获取py拥有的功能",
  },
  pybanben: {
    reg: "^(py|#py)版本$", //匹配消息正则，命令正则
    describe: "【py版本】获取版本日志", //【命令】功能说明
  },
  ...rule1
};
let help_list=[{
  group: "自动执行",
  list: [{
    icon: 61,
    title: "每日60s欣慰推送",
    desc:"默认时间7:30",
  }, {
    icon: 64,
    title: "导入excel版抽卡记录",
    desc: "私聊发送uid命名的excel版抽卡记录，自动合并",
  }, {
    icon: 66,
    title: "自动更新云崽、喵喵、py",
    desc: "默认不强制，需要强制自行开启，提前配置好修改过得文件，可自动备份覆盖",
  }, {
    icon: 67,
    title: "账号冻结自动换号",
    desc: "需要自行配置号相关文件",
  }, {
    icon: 58,
    title: "自动清理",
    desc: "凌晨自动清理当天产生原魔、食物签到等文件，节省空间",
  }]},
  {
    group:"命令",
    list:[]
  }
]
lodash.forEach(rule, (r) => {
  r.priority = r.priority || 50;
  r.prehash = true;
  r.hashMark = true;
  let list={}
  let lists=r.describe.split('】')
  list['icon']=parseInt(lodash.random(0,94))
  list['title']=lists[0].replace('【','')
  list['desc']=lists[1]
  help_list[1].list.push(list)
});
export { rule ,help_list};
const _path = process.cwd();
console.log(`python插件v${currentVersion}为您服务~`);
//const helpFilePath = `${_path}/plugins/python-plugin/resrouces/help/help-list.js`;
let elems=['cryo','electro','geo','hydro','pyro','anemo']
export async function help(e, { render }) {

  if (!/py/.test(e.msg)) {
    return false;
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
  return await Common.render("help/index", {
    helpCfg: helpGroup,
    element: elems[elem1]
  }, { e, render, scale: 1.2 })
}


export async function pybanben(e, { render }) {

  let elem1=lodash.random(0,elems.length-1)
  let elem2=lodash.random(0,elems.length-1)
  return await Common.render("help/version-info", {
    currentVersion,
    changelogs,
    elem: elems[elem1],
    elem1: elems[elem2],
  }, { e, render, scale: 1.2 })
}
