<template lang="html">
  <div
    @click="$emit('clicked')"
    @mouseover="explanationVisible = true"
    @mouseleave="explanationVisible = false"
    class="wrapper"
  >
    <div ref="quad" class="quad">
      <easy-icon :iconName="iconName"></easy-icon>
    </div>
    <div v-if="explanationVisible && desc" class="explanation-wrapper">
      <p class="explanation">
        <slot></slot>
      </p>
    </div>
  </div>
</template>

<script lang="js">
import { defineComponent } from "vue";

export default defineComponent({
  name: "easy-button",

  data() {
    return {
      explanationVisible: false,
    };
  },

  props: {
    iconName: {
      type: String,
      default: "thunder",
    },
    desc: {
      type: Boolean,
      default: false,
    },
    style: {
      type: String,
      default: "gray",
    },
  },

  mounted() {
    this.$refs.quad.classList.add(this.style);
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

.quad {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 0.5em;
  transition: all 0.3s ease-in-out;
}

.quad.gray {
  background-color: rgb(230, 230, 230);
}
.quad.gray:hover {
  background-color: #ffc239;
}

.quad.red {
  background-color: #ffc239;
}
.quad.red:hover {
  opacity: 0.7;
}

.quad.green {
  background-color: #b3ef33;
}
.quad.green:hover {
  opacity: 0.7;
}

.explanation-wrapper {
  position: absolute;
  width: 160%;
  top: calc(100% + 8px);
  left: -30%;
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
  border-color: transparent transparent rgb(230, 230, 230) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 6px);
}

.explanation {
  font-family: "Comfortaa", cursive;
  font-weight: 500;
  user-select: none;
  background-color: rgb(230, 230, 230);
  margin: 0;
  padding: 0.6em;
  text-align: center;
  border-radius: 0.7em;
}
</style>
