import { segment } from "oicq";
import { createRequire } from "module";
import fs from "fs";
import { exec } from "child_process";
const require = createRequire(import.meta.url);
const _path = process.cwd();

export async function huanying(e) {
	if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    	let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    	if(cfg['幻影']=='关闭'){return false;}
  	}
	if (!e.img) {return}
	let img=e.img
	if (img.length<1) {return}
  let command = "python ./plugins/python-plugin/py/huanying.py "+img[0]+' '+img[1];
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{

      let msg = [
      	stdout,
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/1.png`),
        ];
      e.reply(msg)
      return true;
    }
  })
  
}