<template lang="html">
  <Transition name="slide-fade">
    <div v-if="visible" class="wrapper">
      <p>{{ msgData }}</p>
    </div>
  </Transition>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "easy-msg",

  data() {
    return {
      msgData: "",
      visible: false,
      msgStack: 0,
    };
  },

  props: {
    msg: {
      type: String,
      default: "",
    },
    msgTime: {
      type: Number,
      default: 0,
    },
  },

  methods: {
    showMsg(msg: string) {
      this.msgData = msg;
      this.visible = true;
    },
    hideMsg() {
      this.visible = false;
      this.msgStack--;
    },
  },

  watch: {
    msgTime: function (newVal, oldVal) {
      setTimeout(this.showMsg, this.msgStack * 3000, this.msg);
      setTimeout(this.hideMsg, this.msgStack * 3000 + 3000);
      this.msgStack++;
    },
  },
});
</script>

<style lang="css" scoped>
.wrapper {
  position: absolute;
  max-width: 20%;
  max-height: 10%;
  top: 0.5em;
  right: 0.5em;
  background-color: rgb(220, 220, 220);
  border-radius: 0.5em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

p {
  margin: 0;
  padding: 0.4em 0.7em;
  text-decoration: none;
  font-family: "Quicksand", sans-serif;
  font-size: 0.9em;
}

.slide-fade-enter-active {
  transition: all 0.2s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.6s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
