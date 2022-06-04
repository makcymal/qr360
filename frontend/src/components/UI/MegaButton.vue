<template lang="html">
  <div
    @click="$emit('clicked')"
    @mouseover="explanationVisible = true"
    @mouseleave="explanationVisible = false"
    class="filler"
  >
    <div v-for="icon in icons" :key="icon.name" class="filler">
      <div v-if="icon_name == icon.name" class="filler wrapper">
        <img :src="icon.src" class="icon" />
      </div>
    </div>
    <div v-if="explanationVisible" class="explanation-wrapper">
      <p class="explanation">
        {{ description }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: "mega-button",

  data() {
    return {
      explanationVisible: false,
      icons: [{ name: "link", src: require("@/assets/link.svg") }],
    };
  },

  props: {
    icon_name: {
      type: String,
    },
    description: {
      type: String,
      default: "Отправить",
    },
  },
};
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

.filler {
  position: relative;
  width: 100%;
  height: 100%;
}

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(220, 220, 220);
  border-radius: 1em;
  transition: all 0.3s ease-in-out;
}

.wrapper:hover {
  background-color: #ffc239;
}

.icon {
  min-height: 85%;
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
