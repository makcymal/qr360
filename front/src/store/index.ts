import { createStore } from "vuex";
import axios from "axios";
import router from "@/router";
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
    isAuth: false,
    token: "",
    user: {
      username: "test",
      photo_url: "",
    },
    telegramUser: {
      first_name: "",
      last_name: "",
      username: "",
      id: "",
      photo_url: "",
      auth_date: "",
      hash: "",
    },
    qrs: [
      {
        id: "",
        name: "",
        url: "",
        next_url: "",
        next_url_time: "",
        edit_time: 0,
        entries: 0,
        get_image: "",
      },
    ],

    demoQrId: "",
    demoQrImage: "",

    msg: "",
    msgTime: 0,
  },

  mutations: {
    setToken(state, token) {
      state.token = token;
      axios.defaults.headers.common["Authorization"] = "Token " + state.token;
      localStorage.setItem("token", state.token);
    },
  },

  actions: {
    initApp({ state, commit, dispatch }) {
      if (localStorage.getItem("token")) {
        state.isAuth = true;
        commit("setToken", localStorage.getItem("token") as string);
        dispatch("getProfile");
      }
    },

    onAuth({ state, commit }, user: any) {
      axios
        .post("api/users/telegram-auth/", user)
        .then(function (response) {
          if (response.data.success) {
            state.telegramUser = user;
            state.isAuth = true;
            commit("setToken", response.data.token);
            state.user.username = response.data.username;
            state.user.photo_url = response.data.photo_url;
            router.push("/qrs");
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

    logOut({ state }, userData) {
      axios
        .post("api/users/logout/", userData)
        .then(function (response) {
          state.isAuth = false;
          state.token = "";
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.setItem("token", state.token);
          router.push("/");
        })
        .catch(function (error) {
          state.msg =
            "Произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
          state.msgTime = Date.now();
        });
    },

    getProfile({ state }) {
      axios
        .get("api/users/profile/")
        .then(function (response) {
          state.user = {
            username: response.data.username,
            photo_url: response.data.photo_url,
          };
          router.push("/qrs");
        })
        .catch(function (error) {
          // if (error.response) {
          //   for (const property in error.response.data) {
          //     state.msg = `${property}: ${error.response.data[property]}`;
          //     state.msgTime = Date.now();
          //   }
          // } else {
          //   state.msg =
          //     "При авторизации произошла ошибка, пожалуйста, перезагрузите страницу и попробуйте заново";
          //   state.msgTime = Date.now();
          // }
          state.isAuth = false;
          state.token = "";
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.setItem("token", state.token);
          router.push("/");
        });
    },

    getAllQrs({ state }) {
      axios
        .get("api/qrs/")
        .then(function (response) {
          if (response.data.success) {
            state.qrs = response.data.qrs;
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
        .get(`api/qrs/${qrId}/`)
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
        state.msg = "Введите корректную ссылку";
        state.msgTime = Date.now();
        return;
      }

      qr.edit_time = Date.now();

      axios
        .post("api/qrs/", qr)
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

    // qr = { id: number, url: string, name: string (optional) }
    updateQr({ state }, qr) {
      if (!isUrlValid(qr.url) || !isUrlValid(qr.next_url)) {
        state.msg = "Введите корректную ссылку";
        state.msgTime = Date.now();
        return;
      }

      qr.edit_time = Date.now();

      if (qr.next_url_time != "" && qr.next_url != "") {
        qr.count = timeTo(qr.next_url_time);

        if (qr.count <= 0) {
          state.msg = "Укажите правильные дату и время";
          state.msgTime = Date.now();
          return;
        }
      }

      axios
        .put(`api/qrs/${qr.id}/`, qr)
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
        .delete(`api/qrs/${qrId}/`)
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

    getDemoQr({ state, dispatch }) {
      if (localStorage.getItem("demoQrId")) {
        state.demoQrId = localStorage.getItem("demoQrId") as string;
      } else if (state.demoQrId === "") {
        dispatch("createDemoQr", "univer.dvfu.ru");
        return;
      }

      axios
        .get(`api/qrs/demo/${state.demoQrId}/`)
        .then(function (response) {
          if (response.data.success) {
            state.demoQrId = response.data.qr.id;
            state.demoQrImage = response.data.qr.get_image;
          } else {
            dispatch("createDemoQr", "univer.dvfu.ru");
          }
        })
        .catch(function (error) {
          state.msg =
            "Не удалось загрузить QR, пожалуйста, перезагрузите страницу";
          state.msgTime = Date.now();
          console.log(error);
        });
    },

    createDemoQr({ state }, qrUrl) {
      const data = {
        url: qrUrl,
      };

      axios
        .post("api/qrs/demo/", data)
        .then(function (response) {
          if (response.data.success) {
            state.demoQrId = response.data.qr.id;
            state.demoQrImage = response.data.qr.get_image;
            localStorage.setItem("demoQrId", state.demoQrId);
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

      const data = {
        url: qrUrl,
      };

      axios
        .put(`api/qrs/demo/${state.demoQrId}/`, data)
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
