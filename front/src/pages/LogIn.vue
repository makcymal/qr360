<template>
  <div class="home-block-wrapper">
    <div class="home-demo-wrapper">
      <div
        @mouseover="explanationVisible = true"
        @mouseleave="explanationVisible = false"
        class="home-demo-title-wrapper"
      >
        <h3 class="home-demo-title sm-font">Войдите</h3>
      </div>

      <div class="maker-input-wrapper">
        <easy-input v-model="login">Имя пользователя</easy-input>
      </div>
      <div class="maker-input-wrapper">
        <easy-input v-model="password" :type="'password'">Пароль</easy-input>
      </div>
      <div class="qrs-button quad-cont-lg">
        <easy-button
          :iconName="'setted_name'"
          :desc="true"
          :style="'red'"
          @clicked="logInUser()"
          >Войти</easy-button
        >
      </div>
      <div class="link-wrapper">
        <h3 class="link sm-font" @click="$router.push('/')">Назад</h3>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/store";

export default defineComponent({
  data() {
    return {
      login: "",
      password: "",
    };
  },
  methods: {
    logInUser() {
      if (this.login === "") {
        store.state.msg = "Имя пользователя отсутствует";
        store.state.msgTime = Date.now();
      } else if (this.password === "") {
        store.state.msg = "Пароль отсутствует";
        store.state.msgTime = Date.now();
      } else {
        const data = {
          login: this.login,
          password: this.password,
        };

        store.dispatch("logIn", data);
      }
    },
  },
});
</script>

<style lang="css" scoped>
.maker-input-wrapper {
  width: 90%;
  margin: 0.5em;
}

.home-block-wrapper {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.home-demo-wrapper {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.home-demo-title-wrapper {
  position: relative;
  padding-bottom: 0.1em;
  margin-bottom: 2em;
}

.home-demo-title {
  margin: 0;
  padding: 0;
  text-align: center;
  user-select: none;
  transition: all 0.2s ease;
}

.qrs-button {
  padding-bottom: 0.1em;
  margin-bottom: 2em;
}

.link-wrapper {
  padding-bottom: 0.1em;
  margin-top: 2em;
  margin: auto;
}

.link {
  text-decoration: none;
  cursor: pointer;
}

.link:hover {
  text-decoration: underline;
}
</style>
