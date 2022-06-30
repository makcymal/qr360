import { createApp } from "vue";
import App from "@/App.vue";
import store from "@/store";
import UI from "@/components/UI";
import router from "@/router";
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";

// axios.defaults.baseURL = "https://api.qr360.tk/";
axios.defaults.baseURL = "http://0.0.0.0:8000";

const app = createApp(App);

UI.forEach((ui) => {
  app.component(ui.name, ui);
});

app.use(store).use(router).mount("#app");
