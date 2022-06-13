<template lang="html">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3 img-wrapper">
        <!-- <img :src="getImage" class="qr-img"> -->
        <!-- delete line below -->
        <img src="@/assets/qr.jpg" class="qr-img" />
        <div class="qr-tools">
          <div class="tool-wrapper">
            <easy-button :iconName="'download'" :desc="true"
              >Скачать .svg</easy-button
            >
          </div>
          <div class="tool-wrapper">
            <easy-button :iconName="'code'" :desc="true"
              >Вставить на сайт</easy-button
            >
          </div>
        </div>
      </div>

      <div class="col-md-9 data-wrapper">
        <div class="input-wrapper">
          <easy-input v-model="inputName" :placeholder="'Введите название'"
            >Название QR кода
          </easy-input>
        </div>
        <div class="input-wrapper">
          <easy-input
            v-model="inputUrl"
            :placeholder="'Введите ссылку'"
          ></easy-input>
        </div>
        <div class="input-wrapper">
          <easy-input
            v-model="inputNextUrl"
            :placeholder="'Введите ссылку для отложенного обновления'"
          ></easy-input>
        </div>
        <div class="input-wrapper">
          <easy-input
            v-model="inputNextUrlTime"
            :placeholder="'Введите время отложенного обновления ссылки'"
          ></easy-input>
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

      inputName: "",
      inputUrl: "",
      inputNextUrl: "",
      inputNextUrlTime: "",
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

          if (this.url != "") this.inputUrl = this.url;
          if (this.name != "") this.inputName = this.name;
          if (this.nextUrl != "") this.inputNextUrl = this.nextUrl;
          if (this.nextUrlTime != "") this.inputNextUrlTime = this.nextUrlTime;
          break;
        }
        this.index++;
      }
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

.tool-wrapper {
  width: 2em;
  height: 2em;
  margin: 0.3em;
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
</style>
