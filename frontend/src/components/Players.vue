<template>
  <div class="container" >
    </br>

    <!-- Button trigger modal -->
    <button v-if="player_button" type="button" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg">
      Додати нового гравця
    </button>
    </br>
    </br>

    <table class="table table-hover" >
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
                <input type="number" class="form-control" id="number"  v-model="form.number">
              </div>
            </div>

            <div class="form-group row">
              <label for="first_name" class="col-sm-3 col-form-label">Призвіще:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="first_name" placeholder="Призвіще" v-model="form.first_name">
              </div>
            </div>

            <div class="form-group row">
              <label for="last_name" class="col-sm-3 col-form-label">Ім'я:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="last_name" placeholder="Ім'я" v-model="form.last_name">
              </div>
            </div>

            <div class="form-group row">
              <label for="middle_name" class="col-sm-3 col-form-label">По-батькові:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="middle_name" placeholder="По-батькові" v-model="form.middle_name">
              </div>
            </div>

            <div class="form-group row">
              <label for="role" class="col-sm-3 col-form-label">Амплуа:</label>
              <div class="col-sm-9">
                <select class="custom-select" id="role" v-model="form.role">
<!--                  <option selected>Виберіть амплуа</option>-->
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
                <input class="form-control" type="date" value="2000-04-11" id="example-date-input" v-model="form.birthday">
              </div>
            </div>

            <div class="form-group row">
              <label for="born_at" class="col-sm-3 col-form-label">Місце народження:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="born_at" placeholder="Місце народження" v-model="form.born_at">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-md-3">
                <label for="weight">Вага в кг:</label>
                <input type="number" class="form-control" id="weight" placeholder="Вага" v-model="form.weight">
              </div>

              <div class="form-group col-md-3">
                <label for="height">Висота в см:</label>
                <input type="number" class="form-control" id="height" placeholder="Висота" v-model="form.height">
              </div>

              <div class="form-group col-md-3">
                <label for="attack">Висота атаки в см:</label>
                <input type="number" class="form-control" id="attack" placeholder="Висота атаки" v-model="form.attack">
              </div>

              <div class="form-group col-md-3">
                <label for="block">Висота блоку в см:</label>
                <input type="number" class="form-control" id="block" placeholder="Висота блоку" v-model="form.block">
              </div>
            </div>

            <div class="d-flex justify-content-end">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox1" v-model="form.is_cap">
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


  </div>


</template>

<script>
import $ from "jquery"
import Modal from "@/components/Modal";
import axios from 'axios';

const headers = {
  'Content-Type': 'application/json',
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
    submitForm: function(b) {
      axios.post(this.store + '/api/v1/players/', this.form, {headers: headers})
        .then((res) => {
          console.log(res)
          if (res.data.status == true) {
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
        this.form.number &&
        this.form.first_name &&
        this.form.last_name &&
        this.form.middle_name &&
        this.form.role &&
        this.form.weight &&
        this.form.height &&
        this.form.attack &&
        this.form.block &&
        this.form.born_at) {
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
