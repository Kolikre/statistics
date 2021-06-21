<template>
  <div v-if="auth" class="container-fluid">

<!--    <div><Header></Header></div>-->


    <table class="table table-bordered">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Гравець</th>
          <th scope="col">Прийом</th>
          <th scope="col">Подача</th>
          <th scope="col">Атака</th>
          <th scope="col">Пас</th>
          <th scope="col">Блок</th>

          <th scope="col">Прийом</th>
          <th scope="col">Подача</th>
          <th scope="col">Атака</th>
          <th scope="col">Пас</th>
          <th scope="col">Блок</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="player in this.players">
          <th scope="row">{{player.number}}</th>
          <td>{{player.first_name}} {{player.last_name}}</td>
          <td>
<!--            DIGS-->
            <button type="button" class="btn btn-success" @click="action(player.uuid, 'positive_dig', player.positive_dig, 'total_dig', player.total_dig)">+</button>
            <button type="button" class="btn btn-warning" @click="action(player.uuid, 'nope', player.positive_dig, 'total_dig', player.total_dig)">/</button>
            <button type="button" class="btn btn-danger" @click="action(player.uuid, 'negative_dig', player.negative_dig, 'total_dig', player.total_dig)">-</button>
          </td>
          <td>
<!--            SERVE-->
            <button type="button" class="btn btn-success" @click="action(player.uuid, 'positive_serve', player.positive_serve, 'total_serve', player.total_serve)">+</button>
            <button type="button" class="btn btn-warning" @click="action(player.uuid, 'nope', player.positive_serve, 'total_serve', player.total_serve)">/</button>
            <button type="button" class="btn btn-danger" @click="action(player.uuid, 'negative_serve', player.negative_serve, 'total_serve', player.total_serve)">-</button>
          </td>
          <td>
<!--            ATTAK-->
            <button type="button" class="btn btn-success" @click="action(player.uuid, 'positive_attack', player.positive_attack, 'total_attack', player.total_attack)">+</button>
            <button type="button" class="btn btn-warning" @click="action(player.uuid, 'nope', player.positive_attack, 'total_attack', player.total_attack)">/</button>
            <button type="button" class="btn btn-danger" @click="action(player.uuid, 'negative_attack', player.negative_attack, 'total_attack', player.total_attack)">-</button>
          </td>
          <td>
<!--            SET-->
            <button type="button" class="btn btn-success" @click="action(player.uuid, 'positive_set', player.positive_set, 'total_set', player.total_set)">+</button>
            <button type="button" class="btn btn-warning" @click="action(player.uuid, 'nope', player.positive_set, 'total_set', player.total_set)">/</button>
            <button type="button" class="btn btn-danger" @click="action(player.uuid, 'negative_set', player.negative_set, 'total_set', player.total_set)">-</button>
          </td>
          <td>
<!--            BLOCK-->
            <button type="button" class="btn btn-success" @click="action(player.uuid, 'positive_block', player.positive_block, 'total_block', player.total_block)">+</button>
            <button type="button" class="btn btn-warning" @click="action(player.uuid, 'nope', player.positive_block, 'total_block', player.total_block)">/</button>
            <button type="button" class="btn btn-danger" @click="action(player.uuid, 'negative_block', player.negative_block, 'total_block', player.total_block)">-</button>
          </td>
          <td v-if="player.index_dig < -33" class="bg-danger font-weight-bold"><h3>{{player.index_dig}} %</h3></td>
          <td v-if="player.index_dig >= -33 && player.index_dig <= 0" class="bg-warning font-weight-bold"><h3>{{player.index_dig}} %</h3></td>
          <td v-if="player.index_dig > 0" class="bg-success font-weight-bold"><h3>{{player.index_dig}} %</h3></td>

          <td v-if="player.index_serve < -33" class="bg-danger font-weight-bold"><h3>{{player.index_serve}} %</h3></td>
          <td v-if="player.index_serve >= -33 && player.index_serve <= 0" class="bg-warning font-weight-bold"><h3>{{player.index_serve}} %</h3></td>
          <td v-if="player.index_serve > 0" class="bg-success font-weight-bold"><h3>{{player.index_serve}} %</h3></td>

          <td v-if="player.index_attack< -33" class="bg-danger font-weight-bold"><h3>{{player.index_attack}} %</h3></td>
          <td v-if="player.index_attack >= -33 && player.index_attack <= 0" class="bg-warning font-weight-bold"><h3>{{player.index_attack}} %</h3></td>
          <td v-if="player.index_attack > 0" class="bg-success font-weight-bold"><h3>{{player.index_attack}} %</h3></td>

          <td v-if="player.index_set < -33" class="bg-danger font-weight-bold"><h3>{{player.index_set}} %</h3></td>
          <td v-if="player.index_set >= -33 && player.index_set <= 0" class="bg-warning font-weight-bold"><h3>{{player.index_set}} %</h3></td>
          <td v-if="player.index_set > 0" class="bg-success font-weight-bold"><h3>{{player.index_set}} %</h3></td>

          <td v-if="player.index_block < -33" class="bg-danger font-weight-bold"><h3>{{player.index_block}} %</h3></td>
          <td v-if="player.index_block >= -33 && player.index_block <= 0" class="bg-warning font-weight-bold"><h3>{{player.index_block}} %</h3></td>
          <td v-if="player.index_block > 0" class="bg-success font-weight-bold"><h3>{{player.index_block}} %</h3></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Header from "@/components/Header";
import $ from "jquery"
import axios from 'axios';
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token ' + localStorage.getItem('auth_token')
}

export default {
  name: "Statistic",
  components: {
      Header,
    },
  data() {
    return {
      team_info: '',
      players: ''
    }
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
  created() {
    $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadPlayers()
    this.color()
  },
  methods: {
    action(uuid, action, val, total_name, total_val){
      val += 1
      total_val += 1
      let action_data = '{"' + action + '":' + val + ',' + '"' + total_name + '":' + total_val + '}'
      axios.put(this.store + '/api/v1/player/' + uuid, action_data, {headers: headers})
      window.location.reload();
    },
    goLogout() {
      localStorage.removeItem("auth_token")
      window.location = "/"
      window.location.reload();
    },
    loadPlayers() {
      $.ajax({
        url: this.store + "/api/v1/players/",
        method: "GET",
        success: (response) => {
          this.players = response
          console.log(response)
          if (response.length >= 18 || !sessionStorage.getItem("team_name")){
            this.player_button = false
          } else {
            this.player_button = true
          }
        }
      });
    },
  }
}
</script>

<style scoped>

</style>
