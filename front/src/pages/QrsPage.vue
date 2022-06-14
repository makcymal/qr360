<template lang="html">
  <div class="container-xl">
    <nav class="navbar">
      <p class="navbar-brand xs-font link" @click="toHome">На главную</p>
      <p class="navbar-brand xs-font">{{ $store.state.user }}</p>
    </nav>

    <div class="title-wrapper">
      <h2 class="title lg-font">Ваши QR коды</h2>
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

    <div class="maker-wrapper">
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
            <qr-card :qrId="qr.id"></qr-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/store";

export default defineComponent({
  name: "qrs-page",

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
.link {
  text-decoration: none;
  transition: all 0.3s ease-in-out;
  cursor: pointer;
}

.link:hover {
  text-decoration: underline;
}

.title-wrapper {
  width: 94%;
  margin: 0 3%;
  height: 50vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.maker-wrapper {
  margin-bottom: 2em;
}
</style>
