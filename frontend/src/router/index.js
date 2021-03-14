import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Team from '@/components/Team'
import Players from '@/components/Players'
import Coaches from '@/components/Coaches'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/team',
      name: 'Team',
      component: Team
    },
    {
      path: '/players',
      name: 'Players',
      component: Players
    },
    {
      path: '/coaches',
      name: 'Coaches',
      component: Coaches
    }
  ]
})
