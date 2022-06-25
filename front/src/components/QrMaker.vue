<template lang="html">
  <p class="maker-toggler">
    <button
      class="btn btn-warning"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#makerForm"
      aria-expanded="false"
      aria-controls="makerForm"
    >
      Создать новый QR код
    </button>
  </p>
  <div class="collapse" id="makerForm">
    <div class="card card-body maker-data-wrapper">
      <div class="maker-input-wrapper">
        <easy-input
          v-model="name"
          :placeholder="'Например: QR для рекламной рассылки'"
          >Название QR кода
        </easy-input>
      </div>
      <div class="maker-input-wrapper">
        <easy-input v-model="url" :placeholder="'Например: univer.dvfu.ru'"
          >Ссылка, по которой QR будет перенаправлять
        </easy-input>
      </div>

      <div class="maker-btns-wrapper">
        <div class="quad-cont-md">
          <easy-button
            :iconName="'thunder'"
            :desc="true"
            :style="'green'"
            @clicked="createQr()"
            >Создать</easy-button
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/store";

export default defineComponent({
  name: "qr-maker",

  data() {
    return {
      name: "",
      url: "",
    };
  },

  methods: {
    createQr() {
      store.dispatch("createQr", {
        url: this.url.trim(),
        name: this.name.trim(),
      });
      this.name = "";
      this.url = "";
    },
  },
});
</script>

<style lang="css" scoped>
.maker-toggler {
  text-align: right;
}

.maker-data-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.maker-input-wrapper {
  width: 90%;
  margin: 0.5em;
}

.maker-btns-wrapper {
  width: 90%;
  margin: 0.5em;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
</style>
