<template>
  <div class="hello">
    <a>Team page</a>
    <div v-if="team">
      <div>
        {{team}}
      </div>
    </div>
    <div v-else>
      <button class="btn btn--primary mx-auto" @click="$refs.modalName.openModal()">Створити команду</button>
    </div>



    <modal ref="modalName">
      <template v-slot:header>
        <h1>Створити команду</h1>
      </template>

      <template v-slot:body>

        <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                    <label for="name">Вкажіть назву команди</label>
                    <input type="text" class="form-control" id="name" placeholder="Назва команди" v-model="form.data.attributes.name">
                </div>
                <div class="form-group">
                    <label for="leagues">Виберіть лігу:</label>
                    <select id="leagues" name="league" v-model="form.data.attributes.league">
                        <option value="super">Супер ліга</option>
                        <option value="high">Вища ліга</option>
                        <option value="first">Перша ліга</option>
                        <option value="second">Друга ліга</option>
                        <option value="student">Студентська ліга</option>
                    </select>
                </div>


                <div class="form-group">
                    <label for="gender">Виберіть стать гравців:</label>
                    <select id="gender" name="gender" v-model="form.data.attributes.gender">
                        <option value="M">Чоловіча</option>
                        <option value="W">Жіноча</option>
                    </select>
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
  name: 'Team',
  components: {
    Modal,
  },
  data() {
    return {
      team: '',
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
        url: "http://127.0.0.1:8000/api/v1/room/",
        method: "GET",
        success: (response) => {
          this.team = response.data.response
          console.log(response)
          if (response.data.response == 0) {
            this.team = false
          }
        }
      });
    },
    submitForm() {
      axios.post('http://127.0.0.1:8000/api/v1/room/', this.form, {headers: headers})
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
