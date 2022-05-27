<template>
	<div class="bg whit-bg">
  	<a href="/" class="to-home">
  		<svg xmlns="http://www.w3.org/2000/svg" fill="black" class="icon" viewBox="0 0 16 16" style="padding: 0.3em 0">
			  <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
			</svg>
			<p class="text xs" style="padding: 0 0.3em">На главную</p>
  	</a>

  	<h1 class="text lrg">Авторизация</h1>
  	<input @input="onInput" v-model="phone" type="text" placeholder="+7 XXX XXX XX XX" class="input sml">

  	<div class="auth-ways-wrapper">
  		<button v-if="authMode == 't'" @click="authChoice('t')" class="btn orng-bg">
  			<p class="text sml whit-fn">Через Telegram</p>
  			<svg xmlns="http://www.w3.org/2000/svg" fill="#FEFEFE" class="icon" viewBox="0 0 16 16">
				  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z"/>
				</svg>
  		</button>

  		<button v-else @click="authChoice('t')" class="btn dgry-bg">
  			<p class="text sml whit-fn">Через Telegram</p>
  			<svg xmlns="http://www.w3.org/2000/svg" fill="#FEFEFE" class="icon" viewBox="0 0 16 16">
				  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z"/>
				</svg>
  		</button>

  		<button v-if="authMode == 'p'" @click="authChoice('p')" class="btn orng-bg">
  			<p class="text sml whit-fn">Ввести пароль</p>
  			<svg xmlns="http://www.w3.org/2000/svg" fill="#FEFEFE" class="icon" viewBox="0 0 16 16">
				  <path d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"/>
				</svg>
  		</button>

  		<button v-else @click="authChoice('p')" class="btn dgry-bg">
  			<p class="text sml whit-fn">Ввести пароль</p>
  			<svg xmlns="http://www.w3.org/2000/svg" fill="#FEFEFE" class="icon" viewBox="0 0 16 16">
				  <path d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"/>
				</svg>
  		</button>
  	</div>

  	<div class="auth-form">
  		<p class="text xs" v-html="authMsg"></p>
  		<input v-if="authMode == 't'" @input="onConf" v-model="conf" type="text" placeholder="Код" class="input sml">
  		<input v-else-if="authMode == 'p'" @input="onConf" v-model="conf"  type="password" placeholder="Пароль" class="input sml">
  		<input v-else :disabled="true" type="text" class="input sml invisible">

  		<button v-if="confIsValid" @click="login" class="login-btn orng-bg active">
  			<p class="text sml whit-fn">Войти</p>
  		</button>
  		<button v-else-if="authMode" class="login-btn lgry-bg">
  			<p class="text sml drgy-fn">Войти</p>
  		</button>
  		<button v-else class="login-btn lgry-bg invisible">
  			<p class="text sml drgy-fn">Войти</p>
  		</button>
  	</div>
  </div>
</template>


<script>
export default {

	data() {
		return {
			phone: "+7 ",
			phoneIsValid: false,
			userExists: false,

			// 't' - telegram, 'p' - password
			authMode: '',
			authMsg: "Введите номер телефона",

			conf: "",
			confIsValid: false,
		}
	},

	methods: {
		onInput(event) {
			this.phone = "+7 "
			let phone_len = 3;
			
			for (var i = 3; i < event.target.value.length && phone_len < 16; ++i) {
				let c = event.target.value[i];
				if ('0' <= c && c <= '9' && event.target.value[i - 1] != '+') {
					if (phone_len == 6 || phone_len == 10 || phone_len == 13) {
						this.phone += ' ';
						phone_len++;
					}
					this.phone += c;
					phone_len++;
				}
			}

			if (phone_len == 16) {
				this.checkPhone();
				this.authMsg = "Выберите способ входа"
				this.phoneIsValid = true;
			}
			else {
				this.authMsg = "Введите номер телефона";
				this.phoneIsValid = false;
			}
			this.authMode = '';
		},

		checkPhone() {
			// request to api for checking if user with this phone already exists
			// ...code...
			// dummy:
			this.userExists = false;
		},

		authChoice(mode) {
			this.conf = "";
			this.confIsValid = false;

			if (!this.phoneIsValid) {
				this.authMsg = "Введите номер телефона";
				this.authMode = '';
				return;
			}

			else if (mode == 't') {

				if (this.userExists)
					this.authMsg = "Введите код, полученный от нашего бота @aboba в личном сообщении";
				else
					this.authMsg = "Напишите /start нашему боту @aboba. <br> Он вышлет в личном сообщении код регистрации";
			}

			else if (mode == 'p') {
				if (this.userExists)
					this.authMsg = "Введите пароль:";
				else
					this.authMsg = "Придумайте пароль. <br> Не меньше 8 символов, хотя бы одна цифра, одна буква и один символ из . , - + /";
			}

			this.authMode = mode;
		},

		onConf() {
			this.confIsValid = false;

			if (this.authMode == 't') {
				if (this.conf.trim().length != 6) {
					this.confIsValid = false;
					return;
				}

				for (var c of this.conf.trim())
					if (!('0' <= c && c <= '9')) {
						this.confIsValid = false;
						return;
					}

				this.confIsValid = true;
			}

			else if (this.authMode == 'p') {
				if (this.conf.trim().length < 8) {
					this.confIsValid = false;
					return;
				}

				let digit = false;
				let alpha = false;
				let sym = false;

				for (var c of this.conf.trim())
					if ('0' <= c && c <= '9')
						digit = true;
					else if ('a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' || 'а' <= c && c <= 'я' || 'А' <= c && c <= 'Я')
						alpha = true;
					else if (c == '.' || c == ',' || c == '-' || c == '+' || c == '/')
						sym = true;
					else {
						this.confIsValid = false;
						return;
					}

				if (digit && alpha && sym)
					this.confIsValid = true;
				else
					this.confIsValid = false;
			}
		},

		login() {
			// user is trying to login or register
			// some actions
		},

	},
}
</script>


<style scoped>
	
.to-home {
	position: absolute;
	top: 1vw;
	left: 1vw;
	display: flex;
	flex-direction: row;
	align-items: center;
	color: black;
	border: 3px solid transparent;
	transition: all 0.2s ease;
}

.to-home:hover {
	border-bottom: 3px solid #FC5819;
}

.input {
	margin: 0.8em 0;
	border: 0;
	border-bottom: 2px solid #282B32;
	outline: none;
	transition: all 0.3s ease;
}

.input:hover,
.input:focus {
	border-bottom-color: #FC5819;
}

.auth-ways-wrapper {
	width: 50vw;
	padding-top: 1em;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}

.btn {
	width: 48%;
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	transition: all 0.3s ease;
}

.btn:hover {
	background-color: #FC5819;
}

.icon {
	width: min(1.8em, 5vh, 2.5vw);
	padding: 0.8em 0;
}

.auth-form {
	width: 80vw;
	height: 10em;
	padding-top: 2em;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	align-items: center;
}

.login-btn {
	padding: 0.5em 0;
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	transition: all 0.3s ease;
}

.login-btn.active:hover {
	background-color: #282B32;
}

</style>