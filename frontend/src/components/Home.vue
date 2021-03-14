<template>
  <div v-if="auth" class="container">

    <div><Header></Header></div>


    <div>
      <h1>WELCOME TO HOME PAGE!!!</h1>
    </div>

  </div>
</template>

<script>
import Header from "@/components/Header";
import $ from "jquery";

export default {
  data() {
    return {
      team_name: ''
    }
  },
  name: 'Home',
  components: {
    Header,
  },
  created() {
    $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
  },
  computed: {
    auth() {
      if (localStorage.getItem("auth_token")){
        return true
      } else {
        this.$router.push({name: "Login"})
      }
    },
    team() {
      if(localStorage.getItem("team_is_created")){
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    goLogout() {
      localStorage.removeItem("auth_token")
      window.location = "/"
      window.location.reload();
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
