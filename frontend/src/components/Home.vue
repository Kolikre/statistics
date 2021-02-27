<template>
  <div v-if="auth" class="container">

    <button v-if="auth" @click="goLogout">Вийти</button>
    <br>
    <div v-if="auth"><Team></Team></div>
    <div class="container">
      <ul class="nav nav-tabs container" id="myTab" role="tablist">
        <li class="nav-item">
          <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">
            Головна
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="profile-tab" data-toggle="tab" href="#players" role="tab" aria-controls="profile" aria-selected="false">
            Список гравців
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">
            Тренери
          </a>
        </li>
      </ul>
  </div>
    <div class="tab-content" id="myTabContent">

      <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
        <h1>WELCOME TO HOME PAGE</h1>
      </div>

      <div class="tab-pane fade" id="players" role="tabpanel" aria-labelledby="profile-tab" data-spy="scroll">
        <Players></Players>
      </div>


      <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
          <Coaches></Coaches>
      </div>


    </div>
    </br>
    </br>

  </div>
</template>

<script>
import Team from "@/components/Team";
import Players from "@/components/Players";
import Coaches from "@/components/Coaches";

export default {
  name: 'Home',
  components: {
    Team,
    Players,
    Coaches,
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
