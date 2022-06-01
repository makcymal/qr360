<template lang="html">
  <div class="bg">
    <div class="container-xl">
      <div class="row">
        <div class="col-md-7 wrapper">
          <div class="main-text">
            <h1 class="title xl-font">QR360</h1>
            <h2 class="desc md-font">Динамические QR коды с собой и навынос</h2>
            <div class="auth">здесь будет кнопка</div>
          </div>
        </div>

        <div class="col-md-5 wrapper">
          <div class="qr-widget">
            <div
              @mouseover="explanationVisible = true"
              @mouseleave="explanationVisible = false"
              class="widget-title-wrapper"
            >
              <h3 class="widget-title sm-font">
                Посмотрите, как это работает:
              </h3>
              <p v-if="explanationVisible" class="explanation xs-font">
                Созданный у нас QR будет вести на промежуточную страницу,
                которая перенаправит пользователя туда, куда укажете Вы!
              </p>
            </div>
            <div class="input-wrapper">
              <text-input v-model="qrQuery"></text-input>
            </div>
            <img src="@/assets/qr-code.gif" class="qrcode" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      explanationVisible: false,
      qrQuery: "",
    };
  },
};
</script>

<style lang="css" scoped>
.bg {
  position: absolute;
  width: 100%;
  height: 100vh;
  top: 0;
  left: 0;
  background-color: #f1f1f1;
  background-image: url("@/assets/bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

.wrapper {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.main-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.title {
  font-weight: 700;
  text-align: center;
}

.desc {
  text-align: center;
}

.auth {
  margin: auto;
  user-select: none;
}

.qr-widget {
  width: 80%;
  height: 70%;
  padding: 1.5em;
  background-color: white;
  border-radius: 2.5em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.widget-title-wrapper {
  position: relative;
  padding-bottom: 0.1em;
  margin-bottom: 2em;
}

.widget-title {
  margin: 0;
  padding: 0;
  text-align: center;
  user-select: none;
  text-decoration: underline;
  transition: all 0.2s ease;
}

.widget-title:hover {
  color: dimgray;
}

.explanation {
  user-select: none;
  background-color: rgb(220, 220, 220);
  position: absolute;
  width: 90%;
  top: calc(100% + 10px);
  left: 5%;
  z-index: 10;
  margin: 0;
  padding: 0.7em;
  text-align: center;
  border-radius: 1em;
}

.explanation:before {
  content: "";
  border-style: solid;
  border-width: 0 8px 12px 8px;
  border-color: transparent transparent rgb(220, 220, 220) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 12px);
}

.input-wrapper {
  width: 90%;
  height: 3em;
}

.qrcode {
  user-select: none;
  width: 65%;
  padding-top: 0.5em;
}
</style>
