import Vue from "../lib/vue.esm.browser";
import { getDemoVue, COMPONENT_NAME } from "../lib/demoBuilder.js";

import { Chart } from "../../www/charts/dataent-charts.min.esm";
import { data as chartsData } from "../../www/charts/data";

dataent.projectDemos = {
	charts: {
		lib: Chart,
		getDemoConfig: (vueContext) => {
			let config = vueContext.config;
			let data = chartsData[vueContext.data];

			config.data = data;
			if(typeof data === "function") {
				config.data = data();
			}

			return {
				config: config,
				options: vueContext.options,
				actions: vueContext.actions
			};
		}
	}
}

let dataPath = document.querySelector("body").getAttribute("data-path");
let projectName = dataPath.slice(0, dataPath.indexOf('/'))

if(projectName in dataent.projectDemos
	&& document.querySelectorAll(COMPONENT_NAME).length) {

	let project = dataent.projectDemos[projectName];

	Vue.component(...Object.values(
		getDemoVue(project.lib, project.getDemoConfig)
	));

	$(document).ready(function( ) {
		dataent.Vue = new Vue().$mount('.page_content');
	});
}
