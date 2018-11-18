<template lang="html">
  <v-layout row wrap>
      <span class="display-2 text-uppercase font-weight-medium">Projects</span>
      <v-btn icon color='blue' dark @click='updateProjectList()'>
        <v-icon>refresh</v-icon>
      </v-btn>
      <v-spacer/>
      <AddProject />
    <v-flex xs12 class='my-3'>
      <v-divider style='border-width: 1.6px 0 0;' />
    </v-flex>
    <v-flex xs12>
      <v-list two-line subheader>

        <v-list-tile avatar @click='openProject(project.id)' 
          v-for='project in projects' :key='project.id'>
          <v-list-tile-avatar>
            <v-icon class="primary lighten-2 grey lighten-1 white--text">folder</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>{{project.name}}</v-list-tile-title>
          </v-list-tile-content>

          <v-list-tile-action>
            <v-layout row>
              <v-btn icon ripple class='mr-4' @click='openProject(project.id)'>
                <v-icon color="grey lighten-1">open_in_browser</v-icon>
              </v-btn>
              <v-btn icon ripple class='mr-3' @click='deleteProject(project.id)'>
                <v-icon color="grey lighten-1">delete</v-icon>
              </v-btn>
            </v-layout>
          </v-list-tile-action>
        </v-list-tile>

      </v-list>
    </v-flex>
  </v-layout>
</template>

<script>
// TODO: show loader on list loading
// TODO: show loader on project deleting

import AddProject from '@/components/AddProject'
import {projectList, projectDelete} from '@/api/project'

export default {
  components:{AddProject},
  data () {
    return {
      TEMP: '',
      projects: [],
    }
  },
  watch: {
    TEMP: {
      handler () {
        this.updateProjectList()
      },
      immediate: true
    }
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
    openProject (id) {
      this.$router.push({
        name: 'projectView',
        params: {id}
      })
    }
  }
}
</script>

<style lang="css">
</style>
