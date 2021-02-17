<template>
  <div class="hello">
    <h1>Home page</h1>
    <button v-if="auth" @click="goLogout">Вийти</button>
    <div v-if="auth"><Team></Team></div>

  </div>
</template>

<script>
import Team from "@/components/Team";

export default {
  name: 'Home',
  components: {
    Team,
  },
  computed: {
    auth() {
      if (localStorage.getItem("auth_token")){
        return true
      } else {
        this.$router.push({name: "Login"})
      }
    }
  },
  methods: {
    goLogout() {
      localStorage.removeItem("auth_token")
      window.location = "/"
    }
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
