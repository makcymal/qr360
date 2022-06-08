import { createStore } from "vuex";
import axios from "axios";

// tg auth validated data example:
// first_name: Максим
// last_name: undefined
// username: the_makcym
// id: 773182128
// photo_url: https://t.me/i/userpic/320/EoXW_hEei9Ranze9sKjLBFiaifvJo4eLEV8VVXSSN3k.jpg
// auth_date: 1654601246
// hash: 3dce944d672e929e9a3a14988668ba8f01c10ca35b75bd0e5f1286f9698880a2

export default createStore({
  state: {
    // чтобы можно было перенаправлять на главную
    isAuth: false,
    sessionHash: "",
    user: Object,
    api: "http://localhost:8000/api/",
    // qr = { id: string, url: string, name: string, entries: value }
    qrs: [{}],
  },
  actions: {
    // works properly
    onAuth({ state, dispatch }, user) {
      console.log(
        `first_name: ${user.first_name} \nlast_name: ${user.last_name} \nusername: ${user.username} \nid: ${user.id} \nphoto_url: ${user.photo_url} \nauth_date: ${user.auth_date} \nhash: ${user.hash}`
      );
      state.isAuth = true;
      state.user = user;

      axios
        .post(state.api + "s", user)
        .then(function (response) {
          state.sessionHash = response.data.hash;
          dispatch("getQrs");
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    // works properly
    getQrs({ state }) {
      axios
        .get(state.api + `qr?hash=${state.sessionHash}`)
        .then(function (response) {
          state.qrs = response.data.qrs;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    // works properly
    // qr = { hash: string, url: string, name: string (optional) }
    createQr({ state, dispatch }, qr) {
      axios
        .post(state.api + "qr", qr)
        .then(function (response) {
          if (response.data.success) {
            dispatch("getQrs");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    // works properly
    // qr = { hash: string, id: number, url: string (optional), name: string (optional) }
    updateQr({ state, dispatch }, qr) {
      axios
        .put(state.api + "qr", qr)
        .then(function (response) {
          if (response.data.success) {
            dispatch("getQrs");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    // works properly
    // qr = { hash: string, id: number }
    deleteQr({ state, dispatch }, qr) {
      axios
        .delete(state.api + "qr", { data: qr })
        .then(function (response) {
          if (response.data.success) {
            dispatch("getQrs");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
});
