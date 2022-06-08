<template lang="html">
  <home-page></home-page>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HomePage from "@/pages/HomePage.vue";

export default defineComponent({
  components: { HomePage },
});
</script>

<style lang="css">
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@500&family=Source+Code+Pro&display=swap");

body {
  margin: 0;
  padding: 0;
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
button {
  padding: 0;
  text-decoration: none;
  font-family: "Quicksand", sans-serif;
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
</style>
