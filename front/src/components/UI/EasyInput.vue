<template lang="html">
  <div class="wrapper">
    <div class="title-wrapper">
      <p class="title">
        <slot></slot>
      </p>
    </div>

    <div class="input-wrapper">
      <input
        type="text"
        spellcheck="false"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :placeholder="placeholder"
      />
      <div class="clear-wrapper">
        <p @click="$emit('update:modelValue', '')" class="clear-btn">×</p>
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
.wrapper {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title-wrapper {
  width: 100%;
  text-align: left;
}

.input-wrapper {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

input {
  width: 100%;
  font-family: "Source Code Pro", monospace;
  font-size: min(1em, 3vw);
  border: 0;
  border-bottom: 2px solid rgb(220, 220, 220);
  outline: none;
}

input:hover,
input:focus {
  border-bottom-color: #ffc239;
}

.clear-wrapper {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.clear-btn {
  user-select: none;
  padding: 0 0.2em;
  margin: 0;
  cursor: pointer;
  font-size: min(1.4em, 5vw);
  color: black;
  transition: all 0.2s ease;
}

.clear-btn:hover {
  color: #ffc239;
}
</style>
