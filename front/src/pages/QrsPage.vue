<template lang="html">
  <div class="qrs-bg"></div>

  <div class="container-fluid qrs-navbar-wrapper">
    <div class="container-xl">
      <nav class="navbar">
        <p class="navbar-brand xs-font qrs-navbar-link" @click="toHome">
          На главную
        </p>
        <p class="navbar-brand xs-font">{{ $store.state.user }}</p>
      </nav>
    </div>
  </div>

  <div class="container-xl">
    <div class="qrs-title-wrapper">
      <h2 class="lg-font">Ваши QR коды</h2>
      <p class="xs-font">Здесь вы можете:</p>
      <ul>
        <li class="xs-font">
          Дать каждому коду название, которое будет видно только вам
        </li>
        <li class="xs-font">
          Задать ссылку, по которой вы бы хотели перенаправлять пользователей
        </li>
        <li class="xs-font">
          Задать ссылку, которая применится в подходящий момент
        </li>
        <li class="xs-font">...а также задать такой момент</li>
      </ul>
    </div>

    <div class="qrs-maker-wrapper">
      <qr-maker></qr-maker>
    </div>

    <div v-for="qr in $store.state.qrs" :key="qr.id" class="accordion">
      <div class="accordion-item">
        <h2 class="accordion-header" :id="`heading-${qr.id}`">
          <button
            v-if="qr.name != ''"
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            :data-bs-target="`#collapse-${qr.id}`"
            aria-expanded="false"
            :aria-controls="`collapse-${qr.id}`"
          >
            {{ qr.name }}
          </button>
          <button
            v-else
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            :data-bs-target="`#collapse-${qr.id}`"
            aria-expanded="false"
            :aria-controls="`collapse-${qr.id}`"
          >
            {{ qr.url }}
          </button>
        </h2>
        <div
          :id="`collapse-${qr.id}`"
          class="accordion-collapse collapse"
          :aria-labelledby="`heading-${qr.id}`"
        >
          <div class="accordion-body">
            <qr-card
              :id="qr.id"
              :name="qr.name"
              :url="qr.url"
              :nextUrl="qr.nextUrl"
              :nextUrlTime="qr.nextUrlTime"
              :entries="qr.entries"
              :getImage="qr.getImage"
            ></qr-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/store";
import QrCard from "@/components/QrCard.vue";
import QrMaker from "@/components/QrMaker.vue";

export default defineComponent({
  name: "qrs-page",

  components: { QrCard, QrMaker },

  methods: {
    toHome() {
      store.state.onHome = true;
    },
  },

  mounted() {
    store.dispatch("getAllQrs");
  },
});
</script>

<style lang="css" scoped>
body {
  padding-bottom: 3em;
}

.qrs-bg {
  position: fixed;
  width: 100vw;
  height: 100vh;
  top: 0;
  left: 0;
  z-index: -1;
  background-color: #f1f1f1;
  background-image: url("@/assets/bg++.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.5;
}

.qrs-navbar-wrapper {
  background-color: white;
}

.qrs-navbar-link {
  text-decoration: none;
  cursor: pointer;
}

.qrs-navbar-link:hover {
  text-decoration: underline;
}

.qrs-title-wrapper {
  width: 94%;
  padding: 0 3%;
  margin: 3em 3%;
  height: 50vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  background-color: white;
  border-radius: 0.4em;
  border: 1px solid lightgray;
}

.qrs-maker-wrapper {
  width: 94%;
  padding: 0 3%;
  margin: 3em 3%;
}
</style>
