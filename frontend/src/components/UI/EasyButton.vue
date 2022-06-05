<template lang="html">
  <div
    @click="$emit('clicked')"
    @mouseover="explanationVisible = true"
    @mouseleave="explanationVisible = false"
    class="wrapper"
  >
    <div class="icon-wrapper">
      <easy-icon :icon_name="icon_name"></easy-icon>
    </div>
    <div
      v-if="explanationVisible && description != ''"
      class="explanation-wrapper"
    >
      <p class="explanation">
        {{ description }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "easy-button",

  data() {
    return {
      explanationVisible: false,
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
    description: {
      type: String,
      default: "",
    },
  },
});
</script>

<style lang="css" scoped>
p {
  margin: 0;
  padding: 0;
  text-decoration: none;
  font-family: "Quicksand", sans-serif;
  font-size: min(0.8em, 2vw);
  line-height: min(1.1em, 2.5vw);
}

.wrapper {
  position: relative;
  user-select: none;
  width: 100%;
  height: 100%;
}

.icon-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(220, 220, 220);
  border-radius: 0.5em;
  transition: all 0.3s ease-in-out;
}

.icon-wrapper:hover {
  background-color: #ffc239;
}

.explanation-wrapper {
  position: absolute;
  width: 120%;
  top: calc(100% + 8px);
  left: -10%;
  z-index: 10;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.explanation-wrapper:before {
  content: "";
  border-style: solid;
  border-width: 0 6px 8px 6px;
  border-color: transparent transparent rgb(220, 220, 220) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 6px);
}

.explanation {
  user-select: none;
  background-color: rgb(220, 220, 220);
  margin: 0;
  padding: 0.6em;
  text-align: center;
  border-radius: 0.7em;
}
</style>
