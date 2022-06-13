import { createApp } from "vue";
import App from "@/App.vue";
import store from "@/store";
import UI from "@/components/UI";
import { BootstrapVue } from 'bootstrap-vue'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

App.use(BootstrapVue);
const app = createApp(App);

UI.forEach((ui) => {
  app.component(ui.name, ui);
});

app.use(store).mount("#app");
