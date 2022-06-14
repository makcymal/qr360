<template lang="html">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3 img-wrapper">
        <img src="@/assets/qr.jpg" class="qr-img" />
        <p class="entries xs-font">Переходов по этому QR: {{ entries }}</p>
        <div class="qr-tools">
          <div class="quad-cont-sm">
            <easy-button :iconName="'download'" :desc="true"
              >Скачать .svg</easy-button
            >
          </div>
          <div class="quad-cont-sm">
            <easy-button :iconName="'code'" :desc="true"
              >Вставить на сайт</easy-button
            >
          </div>
        </div>
      </div>

      <div class="col-md-9 data-wrapper">
        <div class="input-wrapper">
          <easy-input
            v-model="name"
            :placeholder="'Например: QR для рекламной рассылки'"
            >Название QR кода
          </easy-input>
        </div>
        <div class="input-wrapper">
          <easy-input v-model="url" :placeholder="'Например: univer.dvfu.ru'"
            >Ссылка, по которой QR будет перенаправлять
          </easy-input>
        </div>
        <div class="input-wrapper">
          <easy-input
            v-model="nextUrl"
            :placeholder="'Например: github.io/the-makcym/qr'"
            >По этой ссылке QR код будет перенаправлять после указанного времени
          </easy-input>
        </div>
        <div class="input-wrapper">
          <easy-input
            v-model="nextUrlTime"
            :placeholder="'Например: 2012-12-31 17:59'"
            >Время для вышеуказанной ссылки
          </easy-input>
        </div>

        <div class="btns-wrapper">
          <div class="quad-cont-md">
            <easy-button
              :iconName="'thunder'"
              :desc="true"
              :style="'green'"
              @clicked="updateQr()"
              >Сохранить</easy-button
            >
          </div>
          <div class="quad-cont-md">
            <easy-button
              :iconName="'trash'"
              :desc="true"
              :style="'red'"
              @clicked="deleteQr()"
              >Удалить</easy-button
            >
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
  name: "qr-card",

  data() {
    return {
      index: 0,
      name: "",
      url: "",
      nextUrl: "",
      nextUrlTime: "",
      entries: 0,
      getImage: "",
    };
  },

  props: {
    qrId: {
      type: String,
    },
  },

  methods: {
    updateFromStore() {
      this.index = 0;
      for (let qr of store.state.qrs) {
        if (qr.id == this.qrId) {
          this.name = qr.name;
          this.url = qr.url;
          this.nextUrl = qr.next_url;
          this.nextUrlTime = qr.next_url_time;
          this.entries = qr.entries;
          this.getImage = qr.get_image;
          break;
        }
        this.index++;
      }
    },

    updateQr() {
      store.dispatch("updateQr", {
        name: this.name.trim(),
        url: this.url.trim(),
        next_url: this.nextUrl.trim(),
        next_url_time: this.nextUrlTime.trim(),
      });
    },

    deleteQr() {
      store.dispatch("deleteQr", this.qrId);
    },
  },

  mounted() {
    this.updateFromStore();
  },
});
</script>

<style lang="css" scoped>
.img-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.qr-img {
  width: 80%;
  max-width: 40vw;
  padding: 1em;
}

.qr-tools {
  width: 90%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.entries {
  padding-top: 1em;
  font-family: "Comfortaa", cursive;
  font-weight: 500;
}

.data-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.input-wrapper {
  width: 90%;
  margin: 0.5em;
}

.btns-wrapper {
  width: 90%;
  margin: 0.5em;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
</style>
