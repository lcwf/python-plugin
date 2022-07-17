import fs from 'node:fs'
//import {exec} from "child_process";
import base from './base.js'
import {createRequire} from "module";
import PluginsLoader from '../../../lib/plugins/loader.js'
const require = createRequire(import.meta.url);

export default class exepy{
	constructor (e={}) {
	    this.e = e
    	this.userId = e?.user_id
    	this._path = process.cwd().replace(/\\/g, '/')
	    this.model = 'exepy'
	    this.plugins = PluginsLoader
  	}
  	async sleep(ms) {
  		return new Promise((resolve) => setTimeout(resolve, ms));
	}
	async exepy (command){
		var exec = require('child_process').exec;
		return new Promise((resolve,reject)=>{
			exec(command,function(error,stdout,stderr){
				if (error) {
			      	logger.log("失败！\nError code: "+error.code+"\n"+error.stack);
			      	reject(error)
			    }else{
			    	logger.info(stdout)
			    	resolve(stdout)
	    		}
			})
		})		  
  	}
 }		
