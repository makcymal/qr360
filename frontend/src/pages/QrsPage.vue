<template lang="html">
  <div v-for="qr in $store.state.qrs" :key="qr.id">
    <img :src="qr.get_image" />
  </div>
</template>

<script lang="ts">
export default {};
</script>

<style lang="css" scoped></style>
