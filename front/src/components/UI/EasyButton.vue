<template lang="html">
  <div
    @click="$emit('clicked')"
    @mouseover="explanationVisible = true"
    @mouseleave="explanationVisible = false"
    class="easy-button-wrapper"
  >
    <div ref="quad" class="btn-icon-wrapper">
      <easy-icon :iconName="iconName"></easy-icon>
    </div>
    <div v-if="explanationVisible && desc" class="btn-explanation-wrapper">
      <p class="btn-explanation">
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

.easy-button-wrapper {
  position: relative;
  user-select: none;
  width: 100%;
  height: 100%;
}

.btn-icon-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 0.5em;
  transition: all 0.3s ease-in-out;
}

.btn-icon-wrapper.gray {
  background-color: rgb(230, 230, 230);
}
.btn-icon-wrapper.gray:hover {
  background-color: #ffc239;
}

.btn-icon-wrapper.red {
  background-color: #ffc239;
}
.btn-icon-wrapper.red:hover {
  opacity: 0.7;
}

.btn-icon-wrapper.green {
  background-color: #b3ef33;
}
.btn-icon-wrapper.green:hover {
  opacity: 0.7;
}

.btn-explanation-wrapper {
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

.btn-explanation-wrapper:before {
  content: "";
  border-style: solid;
  border-width: 0 6px 8px 6px;
  border-color: transparent transparent rgb(230, 230, 230) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 6px);
}

.btn-explanation {
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
