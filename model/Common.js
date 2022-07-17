import { Cfg } from "./Cfg.js";
import { segment } from "oicq";
//import { currentVersion,yunzaiVersion} from "./Updatelog.js";
import {render1} from "./render.js";
const _path = process.cwd();
export const render = async function (path, params, cfg) {
  let paths = path.split("/");
  let { render, e } = cfg;
  let _layout_path = process.cwd() + "/plugins/python-plugin/resrouces/help/";
  let base64 = await render1(paths[0], paths[1], {
    ...params,
    _layout_path,
    defaultLayout: _layout_path + "default.html",
    elemLayout: _layout_path + "elem.html",
    sys: {
      scale: Cfg.scale(cfg.scale || 1),
      copyright: `Created By Yunzai-Bot<span class="version">yunzai3.0</span> & Python-Plugin<span class="version">py</span>`
    }
  });

  if (base64) {
    //e.reply(segment.image(`base64://${base64}`));
    return segment.image(`base64://${base64}`);
  }

  return true;
}


export default {
  render,
};