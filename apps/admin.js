import { segment } from "oicq";
import { createRequire } from "module";
import fs from "fs";
import { exec } from "child_process";
const require = createRequire(import.meta.url);
const _path = process.cwd();

const checkAuth = async function (e) {
  return await e.checkAuth({
    auth: "master",
    replyMsg: `只有主人才能命令哦~
    (*/ω＼*)`
  });
}
export async function qingli(e) {
  if (!await checkAuth(e)) {
    return true;
  }
  let command = "python ./plugins/python-plugin/py/clearpic.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      e.reply("清理成功！")
      return true;
    }
  })
  
}
let timer;
export async function python_update(e) {
  
  if (!await checkAuth(e)) {
    return false;
  }
  let isForce = e.msg.includes("强制");
  let command = "git  pull";
  if (isForce) {
    command = "git  checkout . && git  pull";
    e.reply("正在执行强制更新操作，请稍等");
  } else {
    e.reply("正在执行更新操作，请稍等");
  }


  exec(command, { cwd: `${_path}/plugins/python-plugin/` }, function (error, stdout, stderr) {
    //console.log(stdout);
    if (/Already up to date/.test(stdout)) {
      e.reply("目前已经是最新版了~");
      return true;
    }
    if (error) {
      e.reply("更新失败！\nError code: " + error.code + "\n" + error.stack + "\n 请稍后重试。");
      return true;
    }
    e.reply("更新成功，尝试重新启动Yunzai以应用更新...");
    timer && clearTimeout(timer);
    redis.set("python:restart-msg", JSON.stringify({
      msg: "重启成功，新版python-plugin已经生效",
      qq: e.user_id
    }), { EX: 30 });
    timer = setTimeout(function () {
      let command = "npm run restart";
      exec(command, function (error, stdout, stderr) {
        if (error) {
          if (/Yunzai not found/.test(error)) {
            e.reply("自动重启失败，请手动重启以应用新版python-plugin。请使用 npm run start 命令启动Yunzai-Bot");
          } else {
            e.reply("重启失败！\nError code: " + error.code + "\n" + error.stack + "\n 请稍后重试。");
          }
          return true;
        }
      })
    }, 1000);

  });
  return true;
}
export async function profileCfg(e) {
  if (!await checkAuth(e)) {
    return true;
  }
  let cfg1={
          "黄历": "开启",
          "在哪里": "开启",
          "原魔": "开启",
          "食物": "开启",
          "塔罗牌": "开启",
          "圣遗物":"开启",
          "求签": "开启",
          "表情": "开启",
          "订阅": "开启",
          "签到": "开启",
          "戳一戳": "开启",
          "幻影": "开启",
          "人生重来": "开启",
          "remake":"开启",
          "自动更新失败推送":"关闭",
          "自动强制更新py":"关闭",
          "自动强制更新miao":"关闭",
          "自动强制更新yunzai":"关闭",
         }
  let cfg={};
  if (!fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
         //fs.mkdirSync(`./plugins/python-plugin/data/cfg.json`)
         cfg=cfg1
         fs.writeFileSync("./plugins/python-plugin/data/cfg.json", JSON.stringify(cfg, null, "\t"));
    }else{
      cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
      var data1 =Object.keys(cfg)
      for (var key of data1){
        cfg1[key]=cfg[key]
      }
      cfg=cfg1
    }
    var data =Object.keys(cfg)
    if(e.msg.includes('菜单')){
      let msg=[]
      for(var key of data){
        msg.push(key+':'+cfg[key])
      }
      e.reply(msg.join(',').replace(/,/g,'\n'))
    }
  
  //(好友|群|群聊|陌生人)?\s*(\d*)\s*
  let regRet = /py设置(.*)(开启|关闭)$/.exec(e.msg);
  
  if (!regRet) {
    return;
  }
  let [, target1, actionType] = regRet;
  if (!target1) {
    return
  }
  if(!data.includes(target1)){
    return true;
  }else{
    cfg[target1]=actionType
    fs.writeFileSync("./plugins/python-plugin/data/cfg.json", JSON.stringify(cfg, null, "\t"));
    e.reply(target1+'已经'+actionType)
  }
  
  return true; 
  
}

export async function whitelist(e) {
  if (!await checkAuth(e)) {
    return true;
  }
  let list=[];
  if (e.msg.includes('列表')){
    if (!fs.existsSync(`./plugins/python-plugin/data/whitelist.json`)) {
      e.reply('暂无名单')
      return true;
    }else{
      list= JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/whitelist.json`, "utf8"));
      e.reply(list.join(',').replace(/,/g,'\n'))
      return true;
    }
  }
  let gid=e.msg.match(/(\d+)/g)
  if (!gid[0])return;
  
  if (!fs.existsSync(`./plugins/python-plugin/data/whitelist.json`)) {
      fs.writeFileSync("./plugins/python-plugin/data/whitelist.json", JSON.stringify(list, null, "\t"));
  }else{
      list= JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/whitelist.json`, "utf8"));
  }
  list.push(gid[0])
  fs.writeFileSync("./plugins/python-plugin/data/whitelist.json", JSON.stringify(list, null, "\t"));
  e.reply('每日60s推送添加群聊'+gid[0]+'成功')
  return true;
}

export async function whitelistdelete(e) {
  if (!await checkAuth(e)) {
    return true;
  }
  if (!fs.existsSync(`./plugins/python-plugin/data/whitelist.json`)) {return true;}
  let list = JSON.parse(fs.readFileSync(`${_path}//plugins/python-plugin/data/whitelist.json`, "utf8"));
  let gid=e.msg.match(/(\d+)/g)
  if(!gid){return true;}
  gid=gid[0].toString()
  if(!list.includes(gid)){
    e.reply("未推送群聊"+gid)
    return true;
  }
  list.splice(list.indexOf(gid),1)
  fs.writeFileSync("./plugins/python-plugin/data/whitelist.json", JSON.stringify(list, null, "\t"));
  e.reply("每日60s推送移除群聊"+gid+"成功！")
  return true;
}

