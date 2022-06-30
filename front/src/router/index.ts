import { createRouter, createWebHistory } from "vue-router";

import store from "@/store";

import HomePage from "@/pages/HomePage.vue";
import QrsPage from "@/pages/QrsPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/qrs",
    name: "Qrs",
    component: QrsPage,
    meta: {
      requireLogin: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuth
  ) {
    next({ name: "Home", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
