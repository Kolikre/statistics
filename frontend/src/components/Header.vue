<template>
  <div v-if="auth" class="container">

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#"><Team></Team></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div v-if="team_name" class="navbar-nav">
          <router-link class="nav-link" to="/" tag="button">Головна</router-link>
          <router-link class="nav-link" to="/players" tag="button">Список гравців</router-link>
          <router-link class="nav-link" to="/coaches" tag="button">Список тренерів</router-link>
          <router-link class="nav-link"  to="/statistic" tag="button">Нова статистика</router-link>
        </div>
      </div>
      <button type="button" class=" float-right btn btn-outline-danger" v-if="auth" @click="goLogout">
        Вийти
      </button>
    </nav>
    <br>
    <br>
  </div>
</template>

<script>
import $ from "jquery"
import Team from "@/components/Team";
import axios from 'axios';

const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token ' + localStorage.getItem('auth_token')
}

export default {
  name: "Header",
  data() {
    return {
      team_name: ''
    }
  },
  components: {
    Team,
  },
  created() {
    $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadTeam()
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
    loadTeam() {
      $.ajax({
        url: this.store + "/api/v1/room/",
        method: "GET",
        success: (response) => {
          console.log(response)
          this.team_name = response[0].name
          // if (this.team_name === undefined) {
          //   this.team_name = false
          // } else {
          //   this.team_name = true
          // }
        }
      });
    },
    goLogout() {
      localStorage.removeItem("auth_token")
      sessionStorage.removeItem("team_name")
      sessionStorage.removeItem("team_uuid")

      window.location = "/"
      window.location.reload();
    },
  }
}
</script>

<style scoped>

</style>
