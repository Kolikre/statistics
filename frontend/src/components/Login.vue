<template>
  <div class="hello">
    <input type="text" v-model="login" placeholder="Логін"/>
    <input type="password" v-model="password" placeholder="Пароль"/>
    <button @click="setLogin">Вхід</button>

  </div>
</template>

<script>
import $ from "jquery"

export default {
  name: 'Login',
  data () {
    return {
      login: "",
      password: ""
    }
  },
  methods: {
    setLogin() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login/",
        type: "POST",
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          alert("Авторизовано!!!");
          localStorage.setItem("auth_token", response.data.attributes.auth_token)
          this.$router.push({name: "Home"})
        },
        error: (response) => {
          if (response.status === 400){
            alert("Логін або пароль невірні");
          }
        },
      })
    },
  }
}
</script>


<style scoped>

</style>
