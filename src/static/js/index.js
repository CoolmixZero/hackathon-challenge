import Router from "./paramHashRouter.js";
import Routes from "./routes.js";
import data from './result.json' assert {type: 'json'};

window.router = new Router(Routes,"welcome");
