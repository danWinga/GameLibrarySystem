import Vue from "vue";
import VueRouter from "vue-router";
import SharksComponent from "../components/SharksComponent.vue";
import GamesLibrary from "../components/GamesLibrary.vue";
import MenuComponent from "../components/MenuComponent.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/sharks",
    name: "SharksComponent",
    component: SharksComponent,
  },
  {
    path: "/games",
    name: "GamesLibrary",
    component: GamesLibrary,
  },
  {
    path: "/menu",
    name: "MenuComponent",
    component: MenuComponent,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
