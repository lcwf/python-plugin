import { segment } from "oicq";
import fetch from "node-fetch";
import {createRequire} from "module";

import fs from "fs";
const require = createRequire(import.meta.url);
//项目路径
const _path = process.cwd();


export async function huangli(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['黄历']=='关闭'){return false;}
  }
  let command = "python ./plugins/python-plugin/py/almanac.py";
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/data/data.rar`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{

      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/qianwen/黄历.png`),
        ];
      e.reply(msg)
      return true;
    }
  })
  
}
export async function qiuqian(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['求签']=='关闭'){return false;}
  }
  let command = "python ./plugins/python-plugin/py/draw_lots.py "+e.user_id;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/qianwen/${e.user_id}.png`),
        ];
      e.reply(msg)
      return true;
    }
  })
}
export async function jieqian(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['求签']=='关闭'){return false;}
  }
  let command = "python ./plugins/python-plugin/py/draw_lots.py "+e.user_id;
  const exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout){
        let msg = [
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/qianwen/${e.user_id}.png`),
          ];
        e.reply(msg)
        return true;
      }else{
        let msg = [
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/jieqian/${e.user_id}.png`),
          ];
        e.reply(msg)
        return true;
      }      
    }
  })
}

export async function food(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['食物']=='关闭'){return false;}
  }
  //let msg1 =e.msg.replace(/#| |/g, "");
  let msg1 =e.msg.replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  
  let command = "python ./plugins/python-plugin/py/fys.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
        msg1=msg1.replace(/食物/g,"")
        let msg="#"+msg1+"图鉴"
        e.reply("请使用"+msg) 
        return false;
      }else{
      let msg = [
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/food/${msg1.substr(2)}.png`),
          ];
      e.reply(msg)
      return true;      
      }}
  })
}
export async function enemies(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['原魔']=='关闭'){return false;}
  }
 let msg1 =e.msg.replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  //const iconv=require('iconv-lite');{encoding:'binary'},
  let command = "python ./plugins/python-plugin/py/fys.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack,stdout);
    }else{
      if (stdout.trim()=="error"){
        return false;
      }else{
      let msg = [

          stdout,
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/enemies_info/${msg1.substr(2)}.png`),
          ];
        e.reply(msg)     
        return true;
      }}
  })
  
}
export async function enemies_name(e) {
  let string=e.msg.split('别名')
 let msg1 =string[0].replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
 let msg2 =string[1].replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  //const iconv=require('iconv-lite');{encoding:'binary'},
  let command = "python ./plugins/python-plugin/py/yuanmobieming.py "+msg1+" "+msg2;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack,stdout);
    }else  if (stdout.trim()=="error1"){
        e.reply('没有该原魔')
        return false;
      }else if (stdout.trim()=="error2"){
        e.reply('该原魔别名已经存在')
        return false;
      }else{          
        e.reply('原魔别名添加成功')   
        return false;
      }
  })
  
}
export async function artifacts(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['圣遗物']=='关闭'){return false;}
  }
  let msg1 =e.msg.replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let command = "python ./plugins/python-plugin/py/fys.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
        return false;
           
      }else{
        let msg = [
          stdout,
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/artifacts/${msg1.substr(3)}.png`),
          ];
        e.reply(msg) 
        return true;    
      }
      }
  })
}
export async function cailiao(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['在哪里']=='关闭'){return false;}
  }
  let msg1 =e.msg.replace(/#|在|哪|里|有|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let n= msg1.match('渊下宫')?7:msg1.match('层岩')?9:(msg1.match('海岛')||msg1.match('金苹果'))?12:2;
  let msg2=(n==7)?msg1.replace(/渊下宫/,''):(n==12)?(msg1.replace(/海岛/,'').replace(/金苹果/,'')):msg1.replace(/层岩/,'')
  if (e.msg.match('菜单')) msg2='菜单';
  let command = "python ./plugins/python-plugin/py/qrps.py "+msg2+' '+n;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
        return false;
           
      }else{
     let msg = [
          stdout,
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/cailiaodian/${msg2}.jpg`),
          ];
        e.reply(msg)
        return true;    
      
      }}
  })
}

export async function tarot(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['塔罗牌']=='关闭'){return false;}
  }
  await e.reply("开始洗牌")

  await e.reply("牌洗好了，请从78张卡牌中抽取四张,如：#抽取45,67,23,35")     
  return true;
}
export async function tarot1(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['塔罗牌']=='关闭'){return true;}
  }
  let msg1 =e.msg.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let command = "python ./plugins/python-plugin/py/toro/tarot.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
           let msg = ['请选择四张牌'];
            e.reply(msg)
            return false;
      }else{
     let msg = [
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/tarot/torot.jpg`),
          ];
        e.reply(msg) 
        return true;   
      
      }}
  })
}

