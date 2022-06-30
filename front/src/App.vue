<template lang="html">
  <section>
    <router-view></router-view>
  </section>
  <easy-msg :msg="$store.state.msg" :msgTime="$store.state.msgTime"></easy-msg>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/store";
import router from "@/router";

export default defineComponent({
  beforeCreate() {
    store.dispatch("initApp");
  },
});
</script>

<style lang="css">
@import url("https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&family=Source+Code+Pro&display=swap");
body {
  margin: 0;
  padding: 0;
  width: 100vw;
  overflow-x: hidden;
}
button {
  border: 0;
}
h1,
h2,
h3,
h4,
h5,
h6,
p,
a,
button,
li {
  padding: 0;
  margin: 0 0 0.3em 0;
  text-decoration: none;
  font-family: "Comfortaa", cursive;
  font-weight: 500;
  font-size: 1em;
}
.bold {
  font-weight: 600;
}
.xl-font {
  font-size: min(5em, 17vw);
}
.lg-font {
  font-size: min(4em, 13vw);
}
.md-font {
  font-size: min(2em, 8vw);
}
.sm-font {
  font-size: min(1.5em, 4.5vw);
}
.xs-font {
  font-size: min(1em, 3vw);
}
.quad-cont-sm {
  width: 2em;
  height: 2em;
  margin: 0.3em;
}
.quad-cont-md {
  width: 2.5em;
  height: 2.5em;
  margin: 0.5em;
}
.quad-cont-lg {
  width: 3em;
  height: 3em;
  margin: 0.8em;
}
</style>
