<template lang="html">
  <div class="easy-icon-wrapper">
    <div v-if="iconName == 'code'" class="icon-icon-wrapper">
      <img src="@/assets/icons/code.svg" class="icon-icon" />
    </div>
    <div v-if="iconName == 'download'" class="icon-icon-wrapper">
      <img src="@/assets/icons/download.svg" class="icon-icon" />
    </div>
    <div v-if="iconName == 'thunder'" class="icon-icon-wrapper">
      <img src="@/assets/icons/thunder.svg" class="icon-icon" />
    </div>
    <div v-if="iconName == 'trash'" class="icon-icon-wrapper">
      <img src="@/assets/icons/trash.svg" class="icon-icon" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "easy-icon",

  props: {
    iconName: {
      type: String,
      default: "thunder",
    },
  },
});
</script>

<style lang="css" scoped>
.easy-icon-wrapper {
  user-select: none;
  position: relative;
  width: 100%;
  height: 100%;
}

.icon-icon-wrapper {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon-icon {
  width: 60%;
  max-width: 60%;
  height: 60%;
  max-height: 60%;
}
</style>
