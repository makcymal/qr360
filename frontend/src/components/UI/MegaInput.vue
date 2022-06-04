<template lang="html">
  <div class="wrapper">
    <img src="@/assets/link.svg" class="icon" />
    <input
      type="text"
      spellcheck="false"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      placeholder="https://www.dvfu.ru/"
    />
    <div class="clear-wrapper">
      <p @click="$emit('update:modelValue', '')" class="clear-btn">×</p>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: "mega-input",

  props: {
    modelValue: {
      type: String,
    },
  },
};
</script>

<style lang="css" scoped>
.wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.icon {
  user-select: none;
  height: 65%;
  max-width: 8%;
}

input {
  width: 90%;
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
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.clear-btn {
  user-select: none;
  padding: 0;
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
