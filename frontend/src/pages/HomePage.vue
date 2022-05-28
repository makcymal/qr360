<template>
  <div class="bg top whit-bg"></div>
  <div class="bg bot lgry-bg"></div>

  <div class="cols-wrapper">
    <div class="col">
      <div class="cont big blue-bg">
        <h2 class="text sml whit-fn">
          Меняйте
          <br />содержимое <br />QR кода, <br />даже если уже <br />отправили
          <br />его <br />всем <br />друзьям
        </h2>
      </div>
      <div class="cont sml">
        <img src="@/img/qr.svg" class="qr" />
      </div>
    </div>
    <div class="col center">
      <div class="cont big dgry-bg">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="#DFE4EA"
          class="alt"
          viewBox="0 0 16 16"
        >
          <path
            d="M1 13.5a.5.5 0 0 0 .5.5h3.797a.5.5 0 0 0 .439-.26L11 3h3.5a.5.5 0 0 0 0-1h-3.797a.5.5 0 0 0-.439.26L5 13H1.5a.5.5 0 0 0-.5.5zm10 0a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 0-1h-3a.5.5 0 0 0-.5.5z"
          />
        </svg>
        <h1 class="text lrg whit-fn">QR360</h1>
      </div>
    </div>
    <div class="col">
      <div class="cont sml btm">
        <router-link to="/auth" class="btn text sml dgry-bg whit-fn">
          Авторизация
        </router-link>
      </div>
      <div class="cont big orng-bg">
        <h3 class="text mdm whit-fn">Как?</h3>
        <h3 class="text xs pad-top whit-fn">
          Созданный у нас QR будет вести на промежуточную страницу, которая
          направит Вашего клиента туда, куда укажете Вы
        </h3>
      </div>
    </div>
  </div>
</template>

<script></script>

<style scoped>
.bg {
  position: absolute;
  width: 100%;
  left: 0;
}

.bg.top {
  height: 30vh;
  top: 0;
}

.bg.bot {
  height: 70vh;
  bottom: 0;
}

.cols-wrapper {
  position: absolute;
  width: 80%;
  height: 80vh;
  top: 10%;
  left: 10%;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

.col {
  width: 25%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  user-select: none;
}

.col.center {
  justify-content: center;
}

.cont {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.cont.big {
  height: 65%;
}

.cont.sml {
  height: 25%;
}

.qr {
  height: 100%;
}

.alt {
  width: 40%;
}

.text {
  font-family: "Rubik", sans-serif;
  margin: 0;
  letter-spacing: 0.05em;
  padding: 0 max(1.5em, 1vw);
  text-align: center;
}

.lrg {
  font-size: min(3.5em, 9vh, 5vw);
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

.pad-top {
  padding-top: min(1em, 1vh);
}

.btn {
  font-weight: 600;
  letter-spacing: 0;
  padding: max(0.7em, 0.5vh, 0.2vw) max(1em, 0.8vh, 0.5vw);
  border: 0;
  border-radius: 5px;
  transition: all 0.3s ease-out;
}

.btn:hover {
  background-color: #fc5819;
}
</style>
