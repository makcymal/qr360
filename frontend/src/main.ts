import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import UI from "@/components/UI";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App);

UI.forEach((ui) => {
  app.component(ui.name, ui);
});

app.use(router).use(store).mount("#app");
