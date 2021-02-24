<template>
  <div class="container" >
    </br>
    </br>
    <!-- Button trigger modal -->
    <button v-if="player_button" type="button" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg">
      Add new player
    </button>
    </br>
    </br>

    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Гравець</th>
          <th scope="col">Амплуа</th>
          <th scope="col">Висота</th>
          <th scope="col">Вага</th>
          <th scope="col">Висота атаки</th>
          <th scope="col">Висота блоку</th>
          <th scope="col">Капітан</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="player in this.players">
          <th scope="row">{{player.number}}</th>
          <td>{{player.first_name}} {{player.last_name}}</td>
          <td>{{player.role}}</td>
          <td>{{player.height}}</td>
          <td>{{player.weight}}</td>
          <td>{{player.attack}}</td>
          <td>{{player.block}}</td>
          <td>{{player.is_cap}}</td>
        </tr>
      </tbody>
    </table>


<!-- Modal -->
<div class="modal fade bd-example-modal-lg" id="modal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Створення гравця</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Закрити">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">

        <!-- MODAL CONTENT -->
        <div class="form-group row">
          <label for="number" class="col-sm-3 col-form-label">Номер футболки:</label>
          <div class="col-sm-2">
            <input type="number" class="form-control" id="number"  v-model="form.data.attributes.number">
          </div>
        </div>

        <div class="form-group row">
          <label for="first_name" class="col-sm-3 col-form-label">Призвіще:</label>
          <div class="col-sm-9">
            <input type="text" class="form-control" id="first_name" placeholder="Призвіще" v-model="form.data.attributes.first_name">
          </div>
        </div>

        <div class="form-group row">
          <label for="last_name" class="col-sm-3 col-form-label">Ім'я:</label>
          <div class="col-sm-9">
            <input type="text" class="form-control" id="last_name" placeholder="Ім'я" v-model="form.data.attributes.last_name">
          </div>
        </div>

        <div class="form-group row">
          <label for="middle_name" class="col-sm-3 col-form-label">По-батькові:</label>
          <div class="col-sm-9">
            <input type="text" class="form-control" id="middle_name" placeholder="По-батькові" v-model="form.data.attributes.middle_name">
          </div>
        </div>

        <div class="form-group row">
          <label for="role" class="col-sm-3 col-form-label">Амплуа:</label>
          <div class="col-sm-9">
            <select class="custom-select" id="role" v-model="form.data.attributes.role">
  <!--            <option selected>Виберіть амплуа</option>-->
              <option value="OS">Діагональний</option>
              <option value="OH">Догравальний</option>
              <option value="ST">Пасуючий</option>
              <option value="MB">Центральний блокуючий</option>
              <option value="LB">Ліберо</option>
            </select>
          </div>
        </div>

        <div class="form-group row">
          <label for="example-date-input" class="col-sm-3 col-form-label">Дата народження: </label>
          <div class="col-sm-9">
            <input class="form-control" type="date" value="2000-04-11" id="example-date-input" v-model="form.data.attributes.birthday">
          </div>
        </div>

        <div class="form-group row">
          <label for="born_at" class="col-sm-3 col-form-label">Місце народження:</label>
          <div class="col-sm-9">
            <input type="text" class="form-control" id="born_at" placeholder="Місце народження" v-model="form.data.attributes.born_at">
          </div>
        </div>

        <div class="form-row">
          <div class="form-group col-md-3">
            <label for="weight">Вага в кг:</label>
            <input type="number" class="form-control" id="weight" placeholder="Вага" v-model="form.data.attributes.weight">
          </div>

          <div class="form-group col-md-3">
            <label for="height">Висота в см:</label>
            <input type="number" class="form-control" id="height" placeholder="Висота" v-model="form.data.attributes.height">
          </div>

          <div class="form-group col-md-3">
            <label for="attack">Висота атаки в см:</label>
            <input type="number" class="form-control" id="attack" placeholder="Висота атаки" v-model="form.data.attributes.attack">
          </div>

          <div class="form-group col-md-3">
            <label for="block">Висота блоку в см:</label>
            <input type="number" class="form-control" id="block" placeholder="Висота блоку" v-model="form.data.attributes.block">
          </div>
        </div>

        <div class="d-flex justify-content-end">
          <input class="form-check-input" type="checkbox" id="inlineCheckbox1" v-model="form.data.attributes.is_cap">
          <label class="form-check-label" for="inlineCheckbox1">Капітан</label>
        </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Відміна</button>
        <button type="button" class="btn btn-primary" @click="checkForm">Зберегти</button>
      </div>
    </div>
  </div>
</div>

<!--    <a>Players</a>-->
<!--    <div>-->
<!--      <button v-if="player_button" class="btn btn&#45;&#45;primary mx-auto" @click="$refs.modalName.openModal()">Додати гравця</button>-->
<!--      <ol>-->
<!--        <li v-for="player in this.players">{{player}}}</li>-->
<!--      </ol>-->
<!--    </div>-->

<!--    <modal ref="modalName">-->
<!--      <template v-slot:header>-->
<!--        <h1>Створити команду</h1>-->
<!--      </template>-->

<!--      <template v-slot:body>-->

<!--        <form v-on:submit.prevent="submitForm">-->
<!--          <div class="form-group">-->
<!--              <label for="number">Номер футболки:</label>-->
<!--              <input type="number" class="form-control" id="number" placeholder="Номер футболки" v-model="form.data.attributes.number">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="first_name">Призвіще:</label>-->
<!--            <input type="text" class="form-control" id="first_name" placeholder="Призвіще" v-model="form.data.attributes.first_name">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="first_name">Ім'я:</label>-->
<!--            <input type="text" class="form-control" id="last_name" placeholder="Ім'я" v-model="form.data.attributes.last_name">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="middle_name">По-батькові:</label>-->
<!--            <input type="text" class="form-control" id="middle_name" placeholder="По-батькові" v-model="form.data.attributes.middle_name">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="role">Амплуа:</label>-->
<!--            <select id="role" name="role" v-model="form.data.attributes.role">-->
<!--              <option value="OS">Діагональний</option>-->
<!--              <option value="OH">Догравальний</option>-->
<!--              <option value="ST">Пасуючий</option>-->
<!--              <option value="MB">Центральний блокуючий</option>-->
<!--              <option value="LB">Ліберо</option>-->
<!--            </select>-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="birthday">День народження:</label>-->
<!--            <input type="date" value="2000-04-11" class="form-control" id="birthday" v-model="form.data.attributes.birthday">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="weight">Вага в кг:</label>-->
<!--            <input type="number" class="form-control" id="weight" placeholder="Вага" v-model="form.data.attributes.weight">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="height">Висота в см:</label>-->
<!--            <input type="number" class="form-control" id="height" placeholder="Висота" v-model="form.data.attributes.height">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="attack">Висота атаки в см:</label>-->
<!--            <input type="number" class="form-control" id="attack" placeholder="Висота атаки" v-model="form.data.attributes.attack">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="block">Висота блоку в см:</label>-->
<!--            <input type="number" class="form-control" id="block" placeholder="Висота блоку" v-model="form.data.attributes.block">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <label for="born_at">Місце народження:</label>-->
<!--            <input type="text" class="form-control" id="born_at" placeholder="Місце народження" v-model="form.data.attributes.born_at">-->
<!--          </div>-->

<!--          <div class="form-group">-->
<!--            <input type="checkbox" class="form-control" id="is_cap" v-model="form.data.attributes.is_cap">-->
<!--            <label for="is_cap">Капітан</label>-->
<!--          </div>-->

<!--        </form>-->
<!--      </template>-->

<!--      <template v-slot:footer>-->
<!--        <div class="d-flex align-items-center justify-content-between">-->
<!--          <button class="btn btn&#45;&#45;secondary" @click="$refs.modalName.closeModal()">Відміна</button>-->
<!--          <button class="btn btn&#45;&#45;primary" @click="submitForm">Зберегти</button>-->
<!--        </div>-->
<!--      </template>-->
<!--    </modal>-->
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
    submitForm: function(b) {
      axios.post('http://127.0.0.1:8000/api/v1/players/', this.form, {headers: headers})
        .then((res) => {
          console.log(res)
          if (res.data.data.status == true) {
            alert("Гравця успішно створено");
            // Close modal on button click
            $('#modal').hide();
            $('.modal-backdrop').hide();
            this.loadPlayers()
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
