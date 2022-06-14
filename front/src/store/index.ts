import { createStore } from "vuex";
import axios from "axios";
import { isUrlValid, timeTo } from "./storeTools";

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
    onHome: true,
    sessionHash: "",
    user: "the-makcym",
    api: "http://localhost:8000/api/",
    qrs: [
      {
        id: "0",
        name: "",
        url: "aboba.ru",
        next_url: "",
        next_url_time: "",
        entries: 127,
        get_image: "",
        edit_time: 2,
      },
      {
        id: "1",
        name: "jopa",
        url: "bebra.ru",
        next_url: "dvfu.ru",
        next_url_time: "2010-12-31 23.59",
        entries: 0,
        get_image: "",
        edit_time: 1,
      },
    ],

    demoQrId: 0,
    demoQrImage: "",

    msg: "",
    msgTime: 0,
  },

  actions: {
    onAuth({ state, dispatch }, user) {
      state.onHome = false;
      if (user.first_name != "") {
        state.user += user.first_name;
        if (user.last_name != "") state.user += " " + user.last_name;
      } else if (user.username != "") state.user += user.username;

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
            state.qrs.sort((a, b) => a.edit_time - b.edit_time);
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

    // qr = { url: string, name: string (optional) }
    createQr({ state }, qr) {
      if (!isUrlValid(qr.url)) {
        state.msg = "Введите ссылку";
        state.msgTime = Date.now();
        return;
      }
      qr.hash = state.sessionHash;
      axios
        .post(state.api + "qr", qr)
        .then(function (response) {
          if (response.data.success) {
            state.qrs.push(response.data.qr);
            state.msg = "QR создан";
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

    // qr = { id: number, url: string (optional), name: string (optional) }
    updateQr({ state }, qr) {
      qr.hash = state.sessionHash;
      qr.edit_time = Date.now();

      qr.count = timeTo(qr.next_url_time);
      if (qr.count <= 0) {
        state.msg = "Укажите правильные дату и время";
        state.msgTime = Date.now();
        return;
      }

      axios
        .put(state.api + "qr", qr)
        .then(function (response) {
          if (response.data.success) {
            for (let savedQr of state.qrs) {
              if (savedQr.id == qr.id) {
                savedQr = response.data.qr;
                break;
              }
            }
            state.msg = "QR обновлен";
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
          url: "https://github.com/the-makcym/qr",
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
      if (qrUrl == "") {
        return;
      }
      axios
        .put(state.api + "qr", { hash: "demo", id: state.demoQrId, url: qrUrl })
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
