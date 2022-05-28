<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Rubik&display=swap");

body {
  margin: 0;
  padding: 0;
}

button {
  border: 0;
}

a {
  text-decoration: none;
}

.blue-bg {
  background-color: #2ccac3;
}
.dgry-bg {
  background-color: #282b32;
}
.lgry-bg {
  background-color: #dfe4ea;
}
.orng-bg {
  background-color: #fc5819;
}
.whit-bg {
  background-color: #fefefe;
}
.whit-fn {
  color: #fefefe;
}

.bg {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.text {
  font-family: "Rubik", sans-serif;
  margin: 0;
  letter-spacing: 0.05em;
  padding: 0 max(1.5em, 1vw);
  text-align: center;
}

.lrg {
  font-size: min(3em, 8vh, 4vw);
}

.mdm {
  font-size: min(1.8em, 5vh, 2.5vw);
}

.sml {
  font-size: min(1.4em, 4vh, 1.8vw);
}

.xs {
  font-size: min(1.1em, 2.5vh, 1.5vw);
}

.invisible {
  opacity: 0;
}
</style>
