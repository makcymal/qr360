import { createStore } from "vuex";
import axios from "axios";
import { isUrlValid } from "./storeTools";

export default createStore({
  state: {
    onHome: true,
    sessionHash: "",
    user: "",
    api: "https://qr360.pythonanywhere.com/api/",
    qrs: [],

    demoQrId: 0,
    demoQrImage: "",

    msg: "",
    msgTime: 0,
  },

  actions: {
    onAuth({ state, dispatch }, user) {
      state.onHome = false;
      if (user.first_name != undefined) {
        state.user += user.first_name;
        if (user.last_name != undefined) state.user += " " + user.last_name;
      } else if (user.username != undefined) state.user += user.username;

      axios
        .post(state.api + "s", user)
        .then(function (response) {
          if (response.data.success) {
            state.sessionHash = response.data.hash;
            dispatch("getAllQrs");
          } else {
            state.msg =
              "При авторизации произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg =
            "При авторизации произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
          state.msgTime = Date.now();
        });
    },

    getAllQrs({ state }) {
      axios
        .get(state.api + `qrs?hash=${state.sessionHash}`)
        .then(function (response) {
          if (response.data.success) {
            state.qrs = response.data.qrs;
            state.qrs.sort((a, b) => b.edit_time - a.edit_time);
          }
        })
        .catch(function (error) {
          state.msg =
            "Не удалось загрузить QR, пожалуйста, перезагрузите страницу";
          state.msgTime = Date.now();
        });
    },

    getQr({ state }, qrId) {
      axios
        .get(state.api + `qr?hash=${state.sessionHash}&id=${qrId}`)
        .then(function (response) {
          if (response.data.success) {
            for (let savedQr of state.qrs) {
              if (savedQr.id == qrId) {
                savedQr = response.data.qr;
                break;
              }
            }
          } else {
            state.msg =
              "Не удалось загрузить QR, пожалуйста, перезагрузите страницу";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg =
            "Не удалось загрузить QR, пожалуйста, перезагрузите страницу";
          state.msgTime = Date.now();
        });
    },

    // qr = { url: string [, name: string ] }
    createQr({ state }, qr) {
      if (!isUrlValid(qr.url)) {
        state.msg = "Введите корректную ссылку";
        state.msgTime = Date.now();
        return;
      }

      qr.hash = state.sessionHash;
      qr.edit_time = Date.now();

      axios
        .post(state.api + "qr", qr)
        .then(function (response) {
          if (response.data.success) {
            state.qrs.push(response.data.qr);
            state.msg = "QR создан";
            state.msgTime = Date.now();
            state.qrs.sort((a, b) => b.edit_time - a.edit_time);
          } else {
            state.msg =
              "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg =
            "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
          state.msgTime = Date.now();
        });
    },

    // qr = { id: number [, url: string, name: string, next_url: string, next_url_time: string ] }
    updateQr({ state, dispatch }, qr) {
      if (!isUrlValid(qr.url) || !isUrlValid(qr.next_url)) {
        state.msg = "Введите корректную ссылку";
        state.msgTime = Date.now();
        return;
      }

      qr.hash = state.sessionHash;
      qr.edit_time = Date.now();

      axios
        .put(state.api + "qr", qr)
        .then(function (response) {
          if (response.data.success) {
            state.msg = "QR обновлен";
            state.msgTime = Date.now();
            dispatch("getAllQrs");
            state.qrs.sort((a, b) => b.edit_time - a.edit_time);
          } else {
            state.msg =
              "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg =
            "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
          state.msgTime = Date.now();
        });
    },

    deleteQr({ state }, qrId) {
      axios
        .delete(state.api + "qr", {
          data: { hash: state.sessionHash, id: qrId },
        })
        .then(function (response) {
          if (response.data.success) {
            let i = 0;
            for (const savedQr of state.qrs) {
              if (savedQr.id == qrId) {
                state.qrs.splice(i, 1);
                break;
              }
              i++;
            }
            state.msg = "QR удален";
            state.msgTime = Date.now();
          } else {
            state.msg =
              "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg =
            "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
          state.msgTime = Date.now();
        });
    },

    createDemoQr({ state }) {
      axios
        .post(state.api + "qr", {
          hash: "demo",
          url: "github.com/the-makcym/qr",
          edit_time: 0,
        })
        .then(function (response) {
          if (response.data.success) {
            state.demoQrId = response.data.qr.id;
            state.demoQrImage = response.data.qr.get_image;
          } else {
            state.msg = "Произошла ошибка, пожалуйста, перезагрузите страницу";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg = "Произошла ошибка, пожалуйста, перезагрузите страницу";
          state.msgTime = Date.now();
        });
    },

    updateDemoQr({ state }, qrUrl) {
      if (!isUrlValid(qrUrl)) {
        state.msg = "Введите корректную ссылку";
        state.msgTime = Date.now();
        return;
      }

      axios
        .put(state.api + "qr", { hash: "demo", id: state.demoQrId, url: qrUrl, edit_time: 0 })
        .then(function (response) {
          if (response.data.success) {
            state.msg = "Содержимое QR кода обновлено";
            state.msgTime = Date.now();
          } else {
            state.msg = "Произошла ошибка, пожалуйста, перезагрузите страницу";
            state.msgTime = Date.now();
          }
        })
        .catch(function (error) {
          state.msg = "Произошла ошибка, пожалуйста, перезагрузите страницу";
          state.msgTime = Date.now();
        });
    },
  },
});
