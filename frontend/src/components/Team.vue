<template>
  <div class="hello">
    <a>Team page</a>
    ${{team}}
  </div>
</template>

<script>
import $ from "jquery"

export default {
  name: 'Login',
  data() {
    return {
      team: '',
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
        }
      });
    }
  }
}
</script>


<style scoped>

</style>
