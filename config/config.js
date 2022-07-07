import { segment } from "oicq";
import fetch from "node-fetch";
import {createRequire} from "module";
import fs from "fs";
import {beifen} from "../apps/beifenbieming.js";
import { exec } from "child_process";
const require = createRequire(import.meta.url);
import schedule from "node-schedule";
//项目路径
const _path = process.cwd();


schedule.scheduleJob("0 59 23 * * ?",async ()=>{
  let command = "python ./plugins/python-plugin/py/clearpic.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }})

});
async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
schedule.scheduleJob("0 0 7 * * ?",async ()=>{
  let Whitelist=[]
  if (!fs.existsSync(`./plugins/python-plugin/data/whitelist.json`)) {
      return;
  }else{
      Whitelist= JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/whitelist.json`, "utf8"));
  }
    //let grouplist=Bot.gl;
    let url="https://api.2xb.cn/zaob";
    let url_1="https://api.iyk0.com/60s";
    let res=await  fetch(url);
    let res1=await res.json();
    if (res1.msg!='Success'){
      res=await fetch(url_1);
      res1=await res.json()
    };
    if (res1.msg=='Success'){
      let msg = [
        segment.image(res1.imageUrl),
        ];
      for (var key of Whitelist){
     
          await Bot.pickGroup(key).sendMsg(msg);

          await sleep(10000);
  }};
})
schedule.scheduleJob("0 0/30 * * * ?",async ()=>{
  console.log('开始检查推送')
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['订阅']=='关闭'){return true;}
  }
  let command = "python ./plugins/python-plugin/py/bilibili/bilibili-tuisong.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
      return;
    }else if(stdout.trim()!="empty"){
      if (!fs.existsSync(`./plugins/python-plugin/data/tuisong.json`)) {
         return;
      }
        let list = JSON.parse(fs.readFileSync(`${_path}//plugins/python-plugin/data/tuisong.json`, "utf8"));
        var data =Object.keys(list)
        for (var key of data){
          if (list[key]?.video){
            Bot.pickGroup(list[key].gid).sendMsg(list[key].video_url);
            sleep(10000);
          }else if(list[key]?.dynamic){
            Bot.pickGroup(list[key].gid).sendMsg(list[key].dynamic_url);
            sleep(10000);
          }else{
            Bot.pickGroup(list[key].gid).sendMsg(list[key].info);
            sleep(10000);
        }};
        fs.unlink(`./plugins/python-plugin/data/tuisong.json`, (err) => {
          });
        return;
  }});
})


schedule.scheduleJob("0 0/15 * * * ?",async ()=>{
  console.log('开始检查更新')
  let command = "python ./plugins/python-plugin/py/genxin.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
      return;
    }
    let msg=stdout;
    let restart=false;
    let ispush=false;//是否推送更新错误
    let aotofocepy=false; 
    let aotofoceyunzai=false;
    let aotofocemiaomiao=false;
    if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
      let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
      if(cfg['自动强制更新py']=='开启'){aotofocepy=true;}
      if(cfg['自动强制更新miao']=='开启'){aotofocemiaomiao=true;}
      if(cfg['自动强制更新yunzai']=='开启'){aotofoceyunzai=true;}
      if(cfg['自动更新失败推送']=='开启'){ispush=true;}
    }
    if (msg.includes("py")){
      if(aotofocepy){
        let command = "python ./plugins/python-plugin/py/beifen.py 读";
        exec(command, function (error, stdout, stderr){
          if (error) {
            console.log("失败！\nError code: "+error.code+"\n"+error.stack);
          }})
       command = "git checkout . && git  pull";
      }else{command= "git  pull";}
      exec(command, { cwd: `${_path}/plugins/python-plugin/` }, function (error2, stdout, stderr) {
        if (/Already up to date/.test(stdout)) {
          console.log("目前已经是最新版了~");
        }
        if (error) {
          //更新报错，私聊，不想接收消息，可以注释下一行
          if(ispush){
            Bot.pickUser(BotConfig.masterQQ[0]).sendMsg("自动更新py失败！详细请看控制台")
          }
          console.log("自动更新py失败！\nError code: " + error.code + "\n" + error.stack + "\n 请稍后重试。");
        }
        redis.set("python:restart-msg", JSON.stringify({
          msg: "重启成功，新版python-plugin已经生效",
          qq: BotConfig.masterQQ[0],
        }), { EX: 30 });
        if(aotofocepy){
          command = "python ./plugins/python-plugin/py/beifen.py 写";
          exec(command, function (error, stdout, stderr){
            if (error) {
              console.log("失败！\nError code: "+error.code+"\n"+error.stack);
            }
          })
        }
        restart=true;
      })
    }
    if (msg.includes("yunzai")){
      if(aotofoceyunzai){
        command = "python ./plugins/python-plugin/py/beifen.py 读";
        exec(command, function (error4, stdout, stderr){
          if (error) {
            console.log("失败！\nError code: "+error.code+"\n"+error.stack);
          }
        })
        command = "git checkout . && git  pull";
      }else{command= "git  pull";}  
      exec(command, { cwd: `${_path}` }, function (error5, stdout, stderr) {
        if (/Already up to date/.test(stdout)) {
          console.log("目前已经是最新版了~");
        }
        if (error) {
          //更新报错，私聊，不想接收消息，可以注释下一行
          if(ispush){
            Bot.pickUser(BotConfig.masterQQ[0]).sendMsg("自动更新yunzai失败！详细请看控制台");
          }
          console.log("自动更新yunzai失败！\nError code: " + error.code + "\n" + error.stack + "\n 请稍后重试。");
        }
        redis.set("yunzai:restart-msg", JSON.stringify({
          msg: "重启成功，新版yunzai已经生效",
          qq: BotConfig.masterQQ[0],
        }), { EX: 30 });
        if(aotofoceyunzai){
          beifen();
          command = "python ./plugins/python-plugin/py/beifen.py 写";
          exec(command, function (error6, stdout, stderr){
            if (error) {
              console.log("失败！\nError code: "+error.code+"\n"+error.stack);
            }
          })
        }
        restart=true;
      })
    }
    if (msg.includes("miaomiao")){
      if(aotofocemiaomiao){
        command = "python ./plugins/python-plugin/py/beifen.py 读";
        exec(command, function (error, stdout, stderr){
          if (error) {
            console.log("失败！\nError code: "+error.code+"\n"+error.stack);
          }
        })
        command = "git checkout . && git  pull";
      }else{command= "git  pull";}  
      exec(command, { cwd: `${_path}/plugins/miao-plugin/` }, function (error, stdout, stderr) {
        if (/Already up to date/.test(stdout)) {
          console.log("目前已经是最新版了~");
        }
        if (error) {
          //更新报错，私聊，不想接收消息，可以注释下一行
          if(ispush){
            Bot.pickUser(BotConfig.masterQQ[0]).sendMsg("自动更新miaomiao失败！详细请看控制台");
          }
          console.log("自动更新maiomiao失败！\nError code: " + error.code + "\n" + error.stack + "\n 请稍后重试。");
        }
        redis.set("miao:restart-msg", JSON.stringify({
          msg: "重启成功，新版miaomiao-plugin已经生效",
          qq: BotConfig.masterQQ[0],
        }), { EX: 30 });
        if(aotofocemiaomiao){
          command = "python ./plugins/python-plugin/py/beifen.py 写";
          exec(command, function (error, stdout, stderr){
            if (error) {
              console.log("失败！\nError code: "+error9.code+"\n"+error9.stack);
            }
          })
        }
        restart=true;
      })
    }
    //restart=false;//不想更新完自动重启的取消这一行注释就行
    if (restart){
      let timer;
      timer = setTimeout(function () {
        command = "npm run restart";
        exec(command, function (error, stdout, stderr) {
          if (error) {
            if (/Yunzai not found/.test(error)) {
              console.log("自动重启失败，请手动重启以应用新版。请使用 npm run start 命令启动Yunzai-Bot");
            } else {
              console.log("重启失败！详细请看控制台");
            }
          }
        })
      }, 1000);
    }
  })
})
