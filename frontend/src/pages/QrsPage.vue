<template lang="html">
  <div></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/store";

export default defineComponent({
  mounted() {
    store.dispatch("onAuth", {
      first_name: "qwerty",
      username: "maksim",
      id: "123456789",
    });
    // store.dispatch("createQr", {
    //   hash: "12345qwerty",
    //   url: "aboba.ru",
    //   name: "abeba",
    // });
  },
});
</script>

<style lang="css" scoped>
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap");
</style>
