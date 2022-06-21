<template lang="html">
  <div class="home-bg">
    <div class="container-xl">
      <div class="row">
        <div class="col-md-7 home-block-wrapper">
          <div class="home-main-wrapper">
            <h1 class="home-main-title xl-font">QR360</h1>
            <h2 class="home-main-desc md-font">
              Динамические QR коды с собой и навынос
            </h2>
            <div class="home-main-auth">
              <auth-button
                mode="callback"
                telegram-login="QR360_bot"
                @callback="onAuth"
              />
            </div>
          </div>
        </div>

        <div class="col-md-5 home-block-wrapper">
          <div class="home-demo-wrapper">
            <div
              @mouseover="explanationVisible = true"
              @mouseleave="explanationVisible = false"
              class="home-demo-title-wrapper"
            >
              <h3 class="home-demo-title sm-font">
                Посмотрите, как это работает:
              </h3>
              <p
                v-if="explanationVisible"
                class="home-demo-explanation xs-font"
              >
                Созданный у нас QR будет вести на промежуточную страницу,
                которая перенаправит пользователя туда, куда укажете Вы!
              </p>
            </div>
            <div class="home-demo-qr-wrapper">
              <div class="home-demo-input-wrapper">
                <easy-input
                  v-model="demoQrUrl"
                  :placeholder="'Например: univer.dvfu.ru'"
                  @clicked="updateDemoQr()"
                >
                  Куда перенаправлять:
                </easy-input>
              </div>
              <div class="quad-cont-sm">
                <easy-button
                  :iconName="'thunder'"
                  :desc="true"
                  :style="'red'"
                  @clicked="updateDemoQr()"
                  >Обновить</easy-button
                >
              </div>
            </div>
            <img :src="$store.state.demoQrImage" class="home-demo-qr" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import store from "@/store";
import AuthButton from "@/components/AuthButton";

export default defineComponent({
  name: "home-page",

  components: { AuthButton },

  data() {
    return {
      explanationVisible: false,
      demoQrUrl: "",
    };
  },

  methods: {
    onAuth(user) {
      store.dispatch("onAuth", user);
    },

    updateDemoQr() {
      store.dispatch("updateDemoQr", this.demoQrUrl);
      this.demoQrUrl = "";
    },
  },
});
</script>

<style lang="css" scoped>
.home-bg {
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

.home-block-wrapper {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.home-main-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.home-main-title {
  font-weight: 700;
  text-align: center;
}

.home-main-desc {
  text-align: center;
}

.home-main-auth {
  margin: auto;
  user-select: none;
}

.home-demo-wrapper {
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

.home-demo-title-wrapper {
  position: relative;
  padding-bottom: 0.1em;
  margin-bottom: 2em;
}

.home-demo-title {
  margin: 0;
  padding: 0;
  text-align: center;
  user-select: none;
  text-decoration: underline;
  transition: all 0.2s ease;
}

.home-demo-title:hover {
  color: dimgray;
}

.home-demo-explanation {
  user-select: none;
  background-color: rgb(230, 230, 230);
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

.home-demo-explanation:before {
  content: "";
  border-style: solid;
  border-width: 0 8px 12px 8px;
  border-color: transparent transparent rgb(220, 220, 220) transparent;
  position: absolute;
  bottom: 100%;
  left: calc(50% - 12px);
}

.home-demo-qr-wrapper {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.home-demo-input-wrapper {
  width: 85%;
}

.home-demo-qr {
  user-select: none;
  width: 65%;
  padding-top: 0.5em;
}
</style>
