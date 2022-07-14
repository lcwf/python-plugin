import { segment } from "oicq";
import { exec } from "child_process";
import fs from "fs";
import {createRequire} from "module";
const require = createRequire(import.meta.url);
const _path = process.cwd();
//优先级统一50，匹配规则卸载rule1内即可
export const rule1 = {
  examples: {
    reg: "测试", //匹配消息正则，命令正则
    describe: "测试", //【命令】功能说明，菜单内会自动添加
  },
}

//函数需要在index里加载并export
export async function examples(e) {
	//去除非法字符，放置命令注入
	let msg =e.msg.replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
	
	console.log(typeof(e))
	let a=e.toString()
	console.log(a)
	//调用py脚本，并传递参数，每个参数用空格隔开。
  let command = "python ./plugins/python-plugin/examples/commands.py "+a;
  var exec = require('child_process').exec;
  //检查文件是否存在
  //if (fs.existsSync(`./plugins/python-plugin/resrouces/123.py`)) {
  	//上传文件
  	//e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  //}
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
    	//stdout为python打印内容，不宜过多，可以进行简单交互
      e.reply('成功')
      return true;
    }
  })
  
}