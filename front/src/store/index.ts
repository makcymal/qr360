import { createStore } from "vuex";
import axios from "axios";

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
    qrs: [Object],
  },
  getters: {
    userQrs(state){
      return state.qrs;
    },
    qrsCount(state){
      return state.qrs.length;
    },
  },
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

          dispatch("getQrs");
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getQrs({ state }) {
      // работает
      axios
        .get(state.api + `qr?hash=${state.sessionHash}`)
        .then(function (response) {
          console.log(response.data);
          state.qrs = response.data.qrs;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    // qr = { hash: "", url: "", name: "" (optional) }
    createQr({ state, dispatch }, qr) {
      console.log(qr);
      axios
        .post(state.api + "qr", qr)
        .then(function (response) {
          console.log(response.data);
          // dispatch("getQrs");
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    delQr({state}, qr){
      for(let i=0; i<state.qrs.length; ++i){
        if(state.qrs[i] === qr){
          delete(state.qrs[i]);
          break;
        }
      }
    }
  },
});
