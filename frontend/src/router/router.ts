import HomePage from "@/pages/HomePage.vue";
import AuthPage from "@/pages/AuthPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: HomePage,
  },
  {
    path: "/auth",
    component: AuthPage,
  },
];

export default createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});
