import { createApp } from "vue";
import App from "@/App.vue";
import store from "@/store";
import UI from "@/components/UI";
import router from "@/router";

import "bootstrap/dist/css/bootstrap.min.css";

const app = createApp(App);

UI.forEach((ui) => {
  app.component(ui.name, ui);
});

app.use(store).use(router).mount("#app");
