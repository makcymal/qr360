import { createApp } from "vue";
import App from "@/App";
import store from "@/store";
import UI from "@/components/UI";

const app = createApp(App);

UI.forEach((ui) => {
  app.component(ui.name, ui);
});

app.use(store).mount("#app");
