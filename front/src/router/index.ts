import { createRouter, createWebHistory } from "vue-router";

import store from "@/store";

import HomePage from "@/pages/HomePage.vue";
import QrsPage from "@/pages/QrsPage.vue";
import CompleteAuth from "@/pages/CompleteAuth.vue";
import LogIn from "@/pages/LogIn.vue";

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
  {
    path: "/complete",
    name: "CompleteAuth",
    component: CompleteAuth,
  },
  {
    path: "/login",
    name: "LogIn",
    component: LogIn,
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
    next({ name: "LogIn", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
