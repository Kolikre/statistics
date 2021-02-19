<template>
  <div class="hello">
    <a>Players</a>
    <div>
      <button v-if="player_button" class="btn btn--primary mx-auto" @click="$refs.modalName.openModal()">Додати гравця</button>
      <ol>
        <li v-for="player in this.players">{{player}}}</li>
      </ol>
    </div>

    <modal ref="modalName">
      <template v-slot:header>
        <h1>Створити команду</h1>
      </template>

      <template v-slot:body>

        <form v-on:submit.prevent="submitForm">
          <div class="form-group">
              <label for="number">Номер футболки:</label>
              <input type="number" class="form-control" id="number" placeholder="Номер футболки" v-model="form.data.attributes.number">
          </div>

          <div class="form-group">
            <label for="first_name">Призвіще:</label>
            <input type="text" class="form-control" id="first_name" placeholder="Призвіще" v-model="form.data.attributes.first_name">
          </div>

          <div class="form-group">
            <label for="first_name">Ім'я:</label>
            <input type="text" class="form-control" id="last_name" placeholder="Ім'я" v-model="form.data.attributes.last_name">
          </div>

          <div class="form-group">
            <label for="middle_name">По-батькові:</label>
            <input type="text" class="form-control" id="middle_name" placeholder="По-батькові" v-model="form.data.attributes.middle_name">
          </div>

          <div class="form-group">
            <label for="role">Амплуа:</label>
            <select id="role" name="role" v-model="form.data.attributes.role">
              <option value="OS">Діагональний</option>
              <option value="OH">Догравальний</option>
              <option value="ST">Пасуючий</option>
              <option value="MB">Центральний блокуючий</option>
              <option value="LB">Ліберо</option>
            </select>
          </div>

          <div class="form-group">
            <label for="birthday">День народження:</label>
            <input type="date" value="2000-04-11" class="form-control" id="birthday" v-model="form.data.attributes.birthday">
          </div>

          <div class="form-group">
            <label for="weight">Вага в кг:</label>
            <input type="number" class="form-control" id="weight" placeholder="Вага" v-model="form.data.attributes.weight">
          </div>

          <div class="form-group">
            <label for="height">Висота в см:</label>
            <input type="number" class="form-control" id="height" placeholder="Висота" v-model="form.data.attributes.height">
          </div>

          <div class="form-group">
            <label for="attack">Висота атаки в см:</label>
            <input type="number" class="form-control" id="attack" placeholder="Висота атаки" v-model="form.data.attributes.attack">
          </div>

          <div class="form-group">
            <label for="block">Висота блоку в см:</label>
            <input type="number" class="form-control" id="block" placeholder="Висота блоку" v-model="form.data.attributes.block">
          </div>

          <div class="form-group">
            <label for="born_at">Місце народження:</label>
            <input type="text" class="form-control" id="born_at" placeholder="Місце народження" v-model="form.data.attributes.born_at">
          </div>

          <div class="form-group">
            <input type="checkbox" class="form-control" id="is_cap" v-model="form.data.attributes.is_cap">
            <label for="is_cap">Капітан</label>
          </div>

        </form>
      </template>

      <template v-slot:footer>
        <div class="d-flex align-items-center justify-content-between">
          <button class="btn btn--secondary" @click="$refs.modalName.closeModal()">Відміна</button>
          <button class="btn btn--primary" @click="checkForm">Зберегти</button>
        </div>
      </template>
    </modal>
  </div>


</template>

<script>
import $ from "jquery"
import Modal from "@/components/Modal";
import axios from 'axios';

const headers = {
  'Content-Type': 'application/vnd.api+json',
  'Authorization': 'Token ' + localStorage.getItem('auth_token')
}

export default {
  name: 'Players',
  components: {
    Modal,
  },
  data() {
    return {
      team_info: '',
      players: '',
      player_button: '',
      form: {
        data: {
          "type": "PlayerView",
          "attributes": {
            number: null,
            first_name: null,
            last_name: null,
            middle_name: null,
            role: null,
            birthday: null,
            weigth: null,
            heigth: null,
            attack: null,
            block: null,
            born_at: null,
            is_active: true,
            is_cap: false,
            team_name: sessionStorage.getItem("team_name"),
            team_uuid: sessionStorage.getItem("team_uuid")
          }
        }
      },
    }
  },
  created() {
    $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadPlayers()
  },
  methods: {
    loadPlayers() {
      $.ajax({
        url: this.store + "/api/v1/players/",
        method: "GET",
        success: (response) => {
          this.players = response.data.response
          console.log(response)
          if (response.data.response.length >= 18 || !sessionStorage.getItem("team_name")){
            this.player_button = false
          } else {
            this.player_button = true
          }
        }
      });
    },
    submitForm() {
      axios.post('http://127.0.0.1:8000/api/v1/players/', this.form, {headers: headers})
        .then((res) => {
          console.log(res)
          if (res.data.data.status == true) {
            alert("Гравця успішно створено");
            window.location.reload()
          } else {
            alert("Сталась помилка");
          }
        })
        .catch((error) => {
          console.log(error)
        }).finally(() => {

      });
    },
    checkForm: function(e) {
      if (
        this.form.data.attributes.number &&
        this.form.data.attributes.first_name &&
        this.form.data.attributes.last_name &&
        this.form.data.attributes.middle_name &&
        this.form.data.attributes.role &&
        this.form.data.attributes.weight &&
        this.form.data.attributes.height &&
        this.form.data.attributes.attack &&
        this.form.data.attributes.block &&
        this.form.data.attributes.born_at) {
        this.submitForm()
      } else {
        alert("Будь ласка, заповніть всі поля")
      }
    },
  }
}
</script>


<style scoped>
.btn {
  padding: 8px 16px;
  border-radius: 5px;
}
.btn--primary {
    background-color: green;
    color: #fff;
}
.btn--secondary {
    background-color: #dddd;
    color: #000;
  }


// utilities
.overflow-hidden {
  overflow: hidden;
}
.mx-auto {
  margin-left: auto;
  margin-right: auto;
}
.d-flex {
  display: flex;
}
.align-items-center {
  align-items: center;
}
.justify-content-between {
  justify-content: space-between;
}
</style>
