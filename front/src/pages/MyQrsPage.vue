<template lang="html">
  <div id="qrs-page">
    <h1>My Qrs</h1>
    <div class="qrs" v-for="qr in userQrs">
      <div class="accordion" role="tablist">

        <b-card no-body class="mb-1">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block v-b-toggle.accordion variant="info">{{ qr.title }}</b-button>
          </b-card-header>
          <b-collapse id="accordion" accordion="my-accordion" role="tabpanel">
            <b-card-body>
              <b-button v-on:click="delQr" class="del">Delete qr</b-button>
              <b-card img-src="{{ qr.url }}"></b-card>
              <!-- qr.pic -->
              <b-card-text>{{ qr.text }}</b-card-text>
            </b-card-body>
          </b-collapse>
        </b-card>

      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";
import store from "@/store";

export default defineComponent({
  name: "qrs-page",
  computed: mapGetters(["userQrs", "qrsCount"]),
  methods: mapActions(["getQrs", "delQr"]),

  async mounted(){
    this.getQrs;
  },

});
</script>

<style lang="css" scoped>

.del{
  padding: 10px 20px;
  background-color: red;
  opacity: 0.7; ;
  color: black;
  border: 2px solid black;
  border-radius: 3px;
  user-select: none;
  line-height: 1.5;
  font-size: 1rem;
}
.del:hover{
  cursor: pointer;
  opacity: 1;
  text-decoration: none;
}
.bg {
  position: absolute;
  width: 100%;
  height: 100vh;
  top: 0;
  left: 0;
  background-color: #f1f1f1;
  background-image: url("@/assets/bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

.wrapper {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.main-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.title {
  font-weight: 700;
  text-align: center;
}

.desc {
  text-align: center;
}

.auth {
  margin: auto;
  user-select: none;
}

.qr-widget {
  width: 80%;
  height: 70%;
  padding: 1.5em;
  background-color: white;
  border-radius: 2.5em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.widget-title-wrapper {
  position: relative;
  padding-bottom: 0.1em;
  margin-bottom: 2em;
}

.widget-title {
  margin: 0;
  padding: 0;
  text-align: center;
  user-select: none;
  text-decoration: underline;
  transition: all 0.2s ease;
}

.widget-title:hover {
  color: dimgray;
}

.explanation {
  user-select: none;
  background-color: rgb(220, 220, 220);
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

.explanation:before {
  content: "";
  border-style: solid;
  border-width: 0 8px 12px 8px;
  border-color: transparent transparent rgb(220, 220, 220) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 12px);
}

.input-wrapper {
  width: 100%;
  height: 3em;
}

.qrcode {
  user-select: none;
  width: 65%;
  padding-top: 0.5em;
}
</style>
