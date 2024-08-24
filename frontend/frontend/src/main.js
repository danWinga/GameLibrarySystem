import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// install  bootsrap  fiirst
import "bootstrap/dist/css/bootstrap.css";
import BootstrapVue from "bootstrap-vue";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
