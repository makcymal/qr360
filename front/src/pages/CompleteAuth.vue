<template>
  <div class="home-block-wrapper">
    <div class="home-demo-wrapper">
      <div class="user-photo-wrapper">
        <img :src="$store.state.telegramUser.photo_url" class="user-photo" />
      </div>
      <div
        @mouseover="explanationVisible = true"
        @mouseleave="explanationVisible = false"
        class="home-demo-title-wrapper"
      >
        <h3 class="home-demo-title sm-font">Зарегестрируйтесь</h3>
        <p v-if="explanationVisible" class="home-demo-explanation xs-font">
          После регистрации, вы сможете войти не только через Telegram, но и по
          паролю!
        </p>
      </div>

      <div class="maker-input-wrapper">
        <easy-input v-model="username">Имя пользователя</easy-input>
      </div>
      <div class="maker-input-wrapper">
        <easy-input v-model="password" :type="'password'">Пароль</easy-input>
      </div>
      <div class="maker-input-wrapper">
        <easy-input v-model="password2" :type="'password'"
          >Повторите пароль</easy-input
        >
      </div>
      <div class="quad-cont-lg">
        <easy-button
          :iconName="'setted_name'"
          :desc="true"
          :style="'red'"
          @clicked="registerUser()"
          >Зарегестрироваться</easy-button
        >
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
      username: store.state.telegramUser.username,
      password: "",
      password2: "",
      explanationVisible: false,
    };
  },
  methods: {
    registerUser() {
      if (this.username === "") {
        store.state.msg = "Имя пользователя отсутствует";
        store.state.msgTime = Date.now();
      } else if (this.password === "") {
        store.state.msg = "Пароль отсутствует";
        store.state.msgTime = Date.now();
      } else if (this.password !== this.password2) {
        store.state.msg = "Пароли не совпадают";
        store.state.msgTime = Date.now();
      } else {
        const data = {
          username: this.username,
          password: this.password,
          password_confirm: this.password2,
          telegram_id: String(store.state.telegramUser.id),
          photo_url: store.state.telegramUser.photo_url,
        };

        store.dispatch("completeAuth", data);
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
  text-decoration: underline;
  transition: all 0.2s ease;
}

.home-demo-title:hover {
  color: dimgray;
}

.home-demo-explanation {
  user-select: none;
  background-color: rgb(230, 230, 230);
  position: absolute;
  width: 90%;
  top: calc(100% + 10px);
  left: 5%;
  z-index: 10;
  margin: 0;
  padding: 0.7em;
  text-align: center;
  border-radius: 1em;
}

.home-demo-explanation:before {
  content: "";
  border-style: solid;
  border-width: 0 8px 12px 8px;
  border-color: transparent transparent rgb(220, 220, 220) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 12px);
}

.user-photo-wrapper {
  margin-bottom: 20px;
}

.user-photo {
  border-radius: 50%;
  width: 100px;
  height: 100px;
}
</style>
