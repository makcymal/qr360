import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    // чтобы можно было перенаправлять на главную
    isAuth: false,
    sessionHash: "",
    user: Object,
    api: "http://kchaw.ru/api/",
    qrs: [Object],
  },
  getters: {},
  mutations: {},
  actions: {
    onAuth({ state, commit, dispatch }, user) {
      console.log(
        `first_name: ${user.first_name} \nlast_name: ${user.last_name} \nusername: ${user.username} \nid: ${user.id} \nphoto_url: ${user.photo_url} \nauth_date: ${user.auth_date} \nhash: ${user.hash}`
      );
      state.isAuth = true;
      state.user = user;

      // работает
      axios
        .post(state.api + "s", user)
        .then(function (response) {
          console.log(response.data.hash);
          state.sessionHash = response.data.hash;

          // работает
          axios
            .get(state.api + `qrs?hash=${state.sessionHash}`)
            .then(function (response) {
              console.log(response.data);
              state.qrs = response.data.qrs;
              console.log(state.qrs);
            })
            .catch(function (error) {
              console.log(error);
            });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
});
