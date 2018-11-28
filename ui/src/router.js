import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home.vue'
import Projects from './views/Projects.vue'
import Postgres from './views/Postgres.vue'
import ProjectView from './views/ProjectView.vue'
import ProjectTodos from './views/ProjectTodos.vue'
import ProjectGitStats from './views/ProjectGitStats.vue'
import ProjectAnalyzeVue from './views/ProjectAnalyzeVue.vue'

Vue.use(Router)
//TODO: add title support for every page
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
    },
    {
      path: '/project-view/:id',
      props: true,
      name: 'projectView',
      component: ProjectView,
      children: [
        {
          path: 'todos',
          props: true,
          name: 'projectTodos',
          component: ProjectTodos
        },
        {
          path: 'git/stats',
          props: true,
          name: 'projectGitStats',
          component: ProjectGitStats
        },
        {
          path: 'analyze-vue-code/',
          props: true,
          name: 'projectAnalyzeVue',
          component: ProjectAnalyzeVue
        }
      ]
    }
  ]
})
