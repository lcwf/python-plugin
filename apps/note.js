import fetch from "node-fetch";
import { segment } from "oicq";
import {Note} from "../../xiaoyao-cvs-plugin/apps/Note.js";
import { render } from "../../../lib/render.js";
import fs from "fs";


Bot.on("notice.group.poke", async (e)=> {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['戳一戳']=='关闭'){return false;}
  }
  //console.log(e)
  if(e.group_id!=862438532){return false;}
  if (typeof YunzaiApps == "undefined") {
    return;
  }
  if (e.group.mute_left > 0) {
    return;
  }
  e.isPoke = true;
  e.user_id = e.operator_id;

  if (e.target_id != BotConfig.account.qq) {
    return;
  }

  //黑名单
  if (BotConfig.balckQQ && BotConfig.balckQQ.includes(Number(e.user_id))) {
    return;
  }

  //主人qq
  if (BotConfig.masterQQ && BotConfig.masterQQ.includes(Number(e.user_id))) {
    e.isMaster = true;
  }



  e.sender = { card: "" };

  // 为e绑定checkMsg
  e.getMysApi = async function (cfg) {
    return await Msg.getMysApi(e, cfg);
  }
  e.checkAuth = async function (cfg) {
    return await Msg.checkAuth(e, cfg);
  }.msg = await redis.get(`genshin:uid:${e.operator_id}`);

  let key = `genshin:poke:${e.user_id}`;

  let num = await redis.get(key);
  if (num && num > 2 && !e.isMaster) {
    if (!(await redis.get(`genshin:pokeTips:${e.group_id}`))) {
      e.reply([segment.at(e.user_id), "\n戳太快了，请慢点。。"]);
      redis.set(`genshin:pokeTips:${e.group_id}`, "1", { EX: 120 });
      return;
    }

    await redis.incr(key);
    redis.expire(key, 120);

    return;
  } else {
    await redis.incr(key);
    redis.expire(key, 120);
  }
  //e.reply('https://genshin.honeyhunterworld.com/db/item/i_22/?lang=CHS')
  e.msg='体力'
  await Note(e,{render});

  return;
})