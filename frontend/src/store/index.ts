import { createStore } from "vuex";
const axios = require("axios").default;

export default createStore({
    state: {
        apiPath: "http://localhost:8000/auth/",
        token: "",
        username: "",
    },

    getters: {},

    mutations: {},

    actions: {
        async register({ state, dispatch }, user) {
            await axios
                .post(state.apiPath + "users/", {
                    username: user.username,
                    password: user.password,
                })
                .then(function (response: any) {
                    console.log("Register Successful!");
                    dispatch("login", user);
                })
                .catch(function (error: any) {
                    console.log("Register Error: ");
                    console.log(error);
                });
        },

        async login({ state }, user) {
            await axios
                .post(state.apiPath + "token/login/", {
                    username: user.username,
                    password: user.password,
                })
                .then(function (response: any) {
                    console.log("Login Successful!");
                    state.token = response.data.auth_token;
                    state.username = user.username;
                    localStorage.setItem("token", state.token);
                })
                .catch(function (error: any) {
                    console.log("Login Error: ");
                    console.log(error);
                });
        },
    },
});
