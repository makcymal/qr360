<template lang="html">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3 card-img-wrapper">
        <img :src="getImage" class="card-img" />
        <p class="card-entries xs-font">Переходов по этому QR: {{ entries }}</p>
        <div class="card-tools">
          <div class="quad-cont-sm">
            <easy-button
              :iconName="'download'"
              :desc="true"
              @clicked="downloadImg()"
              >Скачать .svg</easy-button
            >
          </div>
          <div class="quad-cont-sm">
            <easy-button :iconName="'code'" :desc="true" @clicked="copyHtml()"
              >Вставить на сайт</easy-button
            >
          </div>
        </div>
      </div>

      <div class="col-md-9 card-data-wrapper">
        <div class="card-input-wrapper">
          <easy-input
            v-model="inputName"
            :placeholder="'Например: QR для рекламной рассылки'"
            >Название QR кода
          </easy-input>
        </div>
        <div class="card-input-wrapper">
          <easy-input
            v-model="inputUrl"
            :placeholder="'Например: univer.dvfu.ru'"
            >Ссылка, по которой QR будет перенаправлять
          </easy-input>
        </div>
        <div class="card-input-wrapper">
          <easy-input
            v-model="inputNextUrl"
            :placeholder="'Например: github.io/the-makcym/qr'"
            >По этой ссылке QR код будет перенаправлять после указанного времени
          </easy-input>
        </div>
        <div class="card-input-wrapper">
          <easy-input
            v-model="inputNextUrlTime"
            :placeholder="'Например: 2012-12-31 17:59'"
            >Время для вышеуказанной ссылки
          </easy-input>
        </div>

        <div class="card-btns-wrapper">
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
import axios from "axios";

export default defineComponent({
  name: "qr-card",

  data() {
    return {
      inputName: "",
      inputUrl: "",
      inputNextUrl: "",
      inputNextUrlTime: "",
    };
  },

  props: {
    id: {
      type: String,
    },
    name: {
      type: String,
      default: "",
    },
    url: {
      type: String,
      default: "",
    },
    nextUrl: {
      type: String,
      default: "",
    },
    nextUrlTime: {
      type: String,
      default: "",
    },
    entries: {
      type: Number,
      default: 0,
    },
    getImage: {
      type: String,
      default: "",
    },
  },

  methods: {
    updateQr() {
      store.dispatch("updateQr", {
        id: this.id,
        name: this.name.trim(),
        url: this.url.trim(),
        next_url: this.nextUrl.trim(),
        next_url_time: this.nextUrlTime.trim(),
      });
    },

    deleteQr() {
      store.dispatch("deleteQr", this.id);
    },

    downloadImg() {
      axios({
        url: this.getImage,
        method: "GET",
        responseType: "blob",
      }).then((response) => {
        let fileUrl = window.URL.createObjectURL(new Blob([response.data]));
        let fileLink = document.createElement("a");
        fileLink.href = fileUrl;

        fileLink.setAttribute("download", `qr_${this.id}.svg`);
        document.body.appendChild(fileLink);
        fileLink.click();
      });
    },

    copyHtml() {
      navigator.clipboard.writeText(`<img src="${this.getImage}">`);
    },
  },

  mounted() {
    this.inputName = this.name;
    this.inputUrl = this.url;
    this.inputNextUrl = this.nextUrl;
    this.inputNextUrlTime = this.nextUrlTime;
  },

  watch: {
    name: function (newVal, oldVal) {
      this.inputName = this.name;
    },
    url: function (newVal, oldVal) {
      this.inputUrl = this.url;
    },
    nextUrl: function (newVal, oldVal) {
      this.inputNextUrl = this.nextUrl;
    },
    nextUrlTime: function (newVal, oldVal) {
      this.inputNextUrlTime = this.nextUrlTime;
    },
  },
});
</script>

<style lang="css" scoped>
.card-img-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card-img {
  width: 80%;
  max-width: 40vw;
  padding: 1em;
}

.card-entries {
  padding-top: 1em;
  font-family: "Comfortaa", cursive;
  font-weight: 500;
}

.card-tools {
  width: 90%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.card-data-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card-input-wrapper {
  width: 90%;
  margin: 0.5em;
}

.card-btns-wrapper {
  width: 90%;
  margin: 0.5em;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
</style>
