import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home.vue'
import Projects from './views/Projects.vue'
import BuildSQLQuery from './views/BuildSQLQuery.vue'
import Statistics from './views/Statistics.vue'
import Pix2code from './views/Pix2code.vue'
import GuiGenerator from './views/GuiGenerator.vue'

Vue.use(Router)
//TODO: add title support for every page
export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      children: [
        {
          path: '/projects/',
          name: 'projects',
          component: Projects,
        },
        {
          path: '/buildsqlquery/',
          name: 'buildsqlquery',
          component: BuildSQLQuery,
        },
        {
          path: '/statistics/',
          name: 'statistics',
          component: Statistics,
        },
        {
          path: '/pix2code/',
          name: 'pix2code',
          component: Pix2code,
        },
        {
          path: '/guigenerator/',
          name: 'guigenerator',
          component: GuiGenerator,
        }
      ]
    }
  ]
})
