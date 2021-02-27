<template>
  <div class="container" >
    </br>

    <!-- Button trigger modal -->
    <button v-if="coach_button" type="button" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg">
      Додати нового тренера
    </button>
    </br>
    </br>

    <table class="table table-hover" >
      <thead>
        <tr>
          <th scope="col">ПІБ</th>
          <th scope="col">День народження</th>
          <th scope="col">Телефон</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="coach in this.coaches">
          <td>{{coach.first_name}} {{coach.last_name}} {{coach.middle_name}}</td>
          <td>{{coach.birthday}}</td>
          <td>{{coach.phone}}</td>
        </tr>
      </tbody>
    </table>


    <!-- Modal -->
    <div class="modal fade bd-example-modal-lg" id="modal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="cexampleModalLabel">Створення Тренера</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Закрити">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">

            <!-- MODAL CONTENT -->

            <div class="form-group row">
              <label for="cfirst_name" class="col-sm-3 col-form-label">Призвіще:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="cfirst_name" placeholder="Призвіще" v-model="form.data.attributes.first_name">
              </div>
            </div>

            <div class="form-group row">
              <label for="clast_name" class="col-sm-3 col-form-label">Ім'я:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="clast_name" placeholder="Ім'я" v-model="form.data.attributes.last_name">
              </div>
            </div>

            <div class="form-group row">
              <label for="cmiddle_name" class="col-sm-3 col-form-label">По-батькові:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="cmiddle_name" placeholder="По-батькові" v-model="form.data.attributes.middle_name">
              </div>
            </div>

            <div class="form-group row">
              <label for="cexample-date-input" class="col-sm-3 col-form-label">Дата народження: </label>
              <div class="col-sm-9">
                <input class="form-control" type="date" value="2000-04-11" id="cexample-date-input" v-model="form.data.attributes.c_birthday">
              </div>
            </div>

            <div class="form-group row">
              <label for="cborn_at" class="col-sm-3 col-form-label">Місце народження:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" id="cborn_at" placeholder="Місце народження" v-model="form.data.attributes.c_born_at">
              </div>
            </div>


            <div class="d-flex justify-content-end">
              <input class="form-check-input" type="checkbox" id="cinlineCheckbox1" v-model="form.data.attributes.is_main">
              <label class="form-check-label" for="cinlineCheckbox1">Головний</label>
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
  'Content-Type': 'application/vnd.api+json',
  'Authorization': 'Token ' + localStorage.getItem('auth_token')
}

export default {
  name: 'Coaches',
  components: {
    Modal,
  },
  data() {
    return {
      table_count: 0,
      team_info: '',
      coaches: '',
      coach_button: '',
      form: {
        data: {
          "type": "CoachView",
          "attributes": {
            c_first_name: null,
            c_last_name: null,
            c_middle_name: null,
            c_birthday: null,
            c_born_at: null,
            c_phone: null,
            c_is_active: true,
            is_main: false,
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
    this.loadCoaches()
  },
  methods: {
    loadCoaches() {
      $.ajax({
        url: this.store + "/api/v1/coaches/",
        method: "GET",
        success: (response) => {
          this.coaches = response.data.response
          console.log(response)
          if (response.data.response.length >= 10 || !sessionStorage.getItem("team_name")){
            this.coach_button = false
          } else {
            this.coach_button = true
          }
        }
      });
    },
    submitForm: function(b) {
      axios.post(this.store + '/api/v1/coaches/', this.form, {headers: headers})
        .then((res) => {
          console.log(res)
          if (res.data.data.status == true) {
            alert("Гравця успішно створено");
            // Close modal on button click
            $('.modal').hide();
            $('.modal-backdrop').hide();
            this.loadCoaches()
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
        this.form.data.attributes.first_name &&
        this.form.data.attributes.last_name &&
        this.form.data.attributes.middle_name &&
        this.form.data.attributes.phone &&
        this.form.data.attributes.birthday &&
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
