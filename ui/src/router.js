import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home.vue'
import Projects from './views/Projects.vue'
import Postgres from './views/Postgres.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/projects/',
      name: 'projects',
      component: Projects
    },
    {
      path: '/postgres/',
      name: 'postgres',
      component: Postgres
    }
  ]
})
