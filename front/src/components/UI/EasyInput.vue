<template lang="html">
  <div class="easy-input-wrapper">
    <div class="input-title-wrapper">
      <p class="xs-font bold">
        <slot></slot>
      </p>
    </div>

    <div class="input-input-wrapper">
      <input
        type="text"
        spellcheck="false"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :placeholder="placeholder"
        class="input-input"
      />
      <div class="input-clear-wrapper">
        <p @click="$emit('update:modelValue', '')" class="input-clear">×</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "easy-input",

  props: {
    modelValue: {
      type: String,
    },
    placeholder: {
      type: String,
      default: "",
    },
  },
});
</script>

<style lang="css" scoped>
p {
  padding: 0;
  margin: 0;
}

.easy-input-wrapper {
  position: relative;
  width: 100%;
  padding: 1em 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.input-title-wrapper {
  width: 100%;
  text-align: left;
  padding-bottom: 0.5em;
}

.input-input-wrapper {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-input {
  width: 100%;
  font-family: "Source Code Pro", monospace;
  font-size: min(1em, 3vw);
  border: 0;
  border-bottom: 2px solid rgb(220, 220, 220);
  outline: none;
}

.input-input:hover,
.input-input:focus {
  border-bottom-color: #ffc239;
}

.input-clear-wrapper {
  position: absolute;
  height: calc(100% - 2px);
  padding: 0 0.1em;
  top: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
}

.input-clear {
  font-family: "Comfortaa", cursive;
  font-weight: 500;
  user-select: none;
  padding: 0 0.2em;
  margin: 0;
  cursor: pointer;
  font-size: min(1.4em, 5vw);
  color: black;
  transition: all 0.2s ease;
}

.input-clear:hover {
  color: #ffc239;
}
</style>
