<template>
    <button class="btn">
        <p class="text">
            <slot></slot>
        </p>
    </button>
</template>

<script>
export default {
    name: "text-button",

    props: {
        state: {
            // -1: disabled; 0: enabled, inactive; 1: active
            type: number,
        },
    },
};
</script>

<style scoped>
.btn {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

}
</style>
