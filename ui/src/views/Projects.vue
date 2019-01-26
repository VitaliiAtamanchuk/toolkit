<template lang="html">
  <v-container class='pl-0 ml-3 pt-0'>
    <v-layout row>
    <v-navigation-drawer
      v-model="drawer"
      class="pb-0 blue-grey lighten-3 elevation-0"
      floating
      hide-overlay
      stateless
      width="300"
    >
      <v-expansion-panel v-model='projectsPanel'>
        <v-expansion-panel-content>
          <div slot="header" class='font-weight-black'>Projects</div>
          <v-list class="grow">
            <v-list-tile class='mb-4'>
              <AddProject @updateProjectList='updateProjectList' />
            </v-list-tile>
            <v-list-tile
              v-for="project in projects"
              :key="project.id"
            >
              <v-list-tile-title v-text="project.name"></v-list-tile-title>
              <v-list-tile-action>
                <v-layout row>
                  <v-btn icon ripple class='mr-4' @click='openProject(project)'>
                    <v-icon color="grey lighten-1">open_in_browser</v-icon>
                  </v-btn>
                  <v-btn icon ripple class='mr-3' @click='deleteProject(project.id)'>
                    <v-icon color="grey lighten-1">delete</v-icon>
                  </v-btn>
                </v-layout>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel v-model='projectPanel' v-if='selectedProject' class="pb-0 mt-4">
        <v-expansion-panel-content>
          <div slot="header" class='font-weight-black title'>{{selectedProject.name}}</div>
          <v-divider class='mb-2'/>
          <v-btn outline color='primary darken-4' dark small @click='getProjectTodos()'>
            Show all todos
          </v-btn>
          <v-btn outline color='primary darken-4' dark small @click='getProjectGitStats()'>
            Show git stats
          </v-btn>
          <ProjectTreeView :is-tree-loading='isTreeLoading' :items='items' :active.sync='active' />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-navigation-drawer>

    <v-layout column class='ml-4'>
      <CodeAnalyzer :active='active' :project-id='projectId' />
      <v-card v-if='stats.length' class='grey lighten-4 mb-4'>
        <v-expansion-panel :value='0'>
          <v-expansion-panel-content>
            <h2 class='mb-3' slot='header'>
              Git stats
            </h2>
            <ProjectGitStat :stats='stats' />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-card>
      <v-card v-if='todos.length' class='grey lighten-4'>
        <v-expansion-panel :value='0'>
          <v-expansion-panel-content>
            <h2 class='mb-3' slot='header'>
              TODOs
            </h2>
            <ProjectTodos :todos='todos' :authors='authors' />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-card>
    </v-layout>

    </v-layout>
  </v-container>
</template>

<script>
import AddProject from '@/components/AddProject'
import ProjectTreeView from '@/components/ProjectTreeView'
import ProjectTodos from '@/components/ProjectTodos'
import ProjectGitStat from '@/components/ProjectGitStat'
import CodeAnalyzer from '@/components/Projects/CodeAnalyzer'
import { Container, Box } from '@dattn/dnd-grid'
import '@dattn/dnd-grid/dist/dnd-grid.css'
import {projectList, projectDelete, projectGetTree, projectGetGitStat, projectGetTodos} from '@/api/project'

export default {
  components: {
    AddProject,
    CodeAnalyzer,
    ProjectTreeView,
    ProjectTodos,
    ProjectGitStat,
    DndGridContainer: Container,
    DndGridBox: Box
  },
  data () {
    return {
      maxColumnCount: 15,
      maxRowCount: Infinity,
      bubbleUp: true,
      layout: [
        {
          id: 'todos',
          hidden: false,
          pinned: false,
          position: {
            x: 0,
            y: 6,
            w: 8,
            h: 4
          }
        },
        {
          id: 'gitstats',
          hidden: false,
          pinned: false,
          position: {
            x: 0,
            y: 0,
            w: 8,
            h: 6
          }
        }
      ],
      isTreeLoading: false,
      projects: [],
      projectsPanel: 0,
      projectPanel: 0,
      selectedProject: null,
      drawer: true,
      stats: [],
      todos: [],
      active: [],
      authors: [],
      items: []
    }
  },
  computed: {
    projectId () {
      if (!this.selectedProject) {
        return 0
      } else {
        return this.selectedProject.id
      }
    }
  },
  created () {
    this.updateProjectList()
  },
  methods: {
    updateProjectList () {
      projectList().then(resp => {
        this.projects = resp.data.list
      })
    },
    deleteProject (id) {
      projectDelete(id).then(resp => {
        this.updateProjectList()
      })
    },
    openProject (project) {
      this.selectedProject = project
      this.projectsPanel = -1

      this.isTreeLoading = true
      projectGetTree(project.id).then(resp => {
        this.items = resp.data.tree
      }).finally(() => {this.isTreeLoading = false})
    },
    getProjectGitStats () {
      projectGetGitStat(this.selectedProject.id).then(resp => {
        this.stats = resp.data.stats
      })
    },
    getProjectTodos () {
      projectGetTodos(this.selectedProject.id).then(resp => {
        this.todos = resp.data.todos
        this.authors = resp.data.authors
      })
    }
  }
}
</script>
