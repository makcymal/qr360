<template lang="html">
  <div class="container">
    <div v-for="icon in icons" :key="icon.name" class="filler">
      <div v-if="icon_name == icon.name" class="filler wrapper">
        <img :src="icon.src" class="icon" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "easy-icon",

  data() {
    return {
      icons: [
        { name: "calendar", src: require("@/assets/icons/calendar.svg") },
        { name: "copy", src: require("@/assets/icons/copy.svg") },
        { name: "download", src: require("@/assets/icons/download.svg") },
        { name: "empty_name", src: require("@/assets/icons/empty_name.svg") },
        { name: "link", src: require("@/assets/icons/link.svg") },
        { name: "setted_name", src: require("@/assets/icons/setted_name.svg") },
        { name: "stat", src: require("@/assets/icons/stat.svg") },
        { name: "thunder", src: require("@/assets/icons/thunder.svg") },
      ],
    };
  },

  props: {
    icon_name: {
      type: String,
      default: "thunder",
    },
  },
});
</script>

<style lang="css" scoped>
.container {
  user-select: none;
  position: relative;
  width: 100%;
  height: 100%;
}

.filler {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.wrapper {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon {
  width: 70%;
  max-width: 70%;
  height: 70%;
  max-height: 70%;
}
</style>
