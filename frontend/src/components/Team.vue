<template>
  <div class="hello">

    <div v-if="team">
      <div>
        <h1>{{team_name}}</h1>
        <!--  localStorage.setItem("team_is_created", true)  -->
      </div>
    </div>
    <div v-else>
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">
        Створити команду
      </button>
    </div>




    <!-- MODAL WINDOW -->

      <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLongTitle">Створення команди</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">


              <!-- MODAL CONTENT -->
              <div class="container">
                <div class="form-group row">
                  <label for="team_name" class="col-sm-4 col-form-label">Назва команди:</label>
                  <div class="col-sm-12">
                    <input type="text" class="form-control" id="team-name" placeholder="Введіть назву" v-model="form.data.attributes.name">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="role" class="col-sm-4 col-form-label">Ліга:</label>
                  <div class="col-sm-12">
                    <select class="custom-select" id="role" v-model="form.data.attributes.league">с
                  <!--<option selected>Виберіть амплуа</option>-->
                      <option value="super">Супер</option>
                      <option value="high">Вища</option>
                      <option value="first">Перша</option>
                      <option value="second">Друга</option>
                      <option value="student">Студентська</option>
                    </select>
                  </div>
                </div>

                <div class="form-group row">
                  <label for="gender" class="col-sm-4 col-form-label">Виберіть стать:</label>
                  <div class="col-sm-12">
                    <select class="custom-select" id="gender" v-model="form.data.attributes.gender">
                  <!--<option selected>Виберіть амплуа</option>-->
                      <option value="W">Жінки</option>
                      <option value="M">Чоловіки</option>
                    </select>
                  </div>
                </div>
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
  name: 'Team',
  components: {
    Modal,
  },
  data() {
    return {
      team: '',
      team_name: '',
      form: {
        data: {
          "type": "TeamView",
          "attributes": {
            name: null,
            league: null,
            gender: null
          }
        }
      },
    }
  },
  created() {
    $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadTeam()
  },
  methods: {
    loadTeam() {
      $.ajax({
        url: this.store + "/api/v1/room/",
        method: "GET",
        success: (response) => {
          this.team = response.data.response
          this.team_name = response.data.response[0].name
          if (response.data.response == 0) {
            this.team = false
          } else {
            sessionStorage.setItem("team_name", response.data.response[0].name)
            sessionStorage.setItem("team_uuid", response.data.response[0].uuid)
          }
        }
      });
    },
    submitForm() {
      axios.post(this.store + '/api/v1/room/', this.form, {headers: headers})
        .then((res) => {
          console.log(res)
          if (res.data.data.status == true) {
            alert("Команду успішно створено");
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
      if (this.form.data.attributes.name && this.form.data.attributes.league && this.form.data.attributes.gender) {
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
