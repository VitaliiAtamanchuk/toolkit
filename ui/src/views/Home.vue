<template lang="html">
  <v-app>
    <v-navigation-drawer
      dark
      app
      clipped
      class='indigo darken-4'
      stateless
      value="true"
      width='200'
      :mini-variant='mini'
    >
      <v-list class="py-4" dense>
        <v-list-tile>
          <v-layout row justify-center v-if='!mini'>
            <span class='blue-grey--text text--lighten-5 title'>
              <span class='font-weight-light'>Project</span>
              <span class="font-weight-medium">Manager</span>
            </span>
          </v-layout>
          <span class='blue-grey--text text--lighten-5 title ml-2' v-else>
            <span class="font-weight-black">PM</span>
          </span>
        </v-list-tile>
      </v-list>
      <v-list class="pt-0" dense>
        <v-divider></v-divider>

        <v-list-tile
          v-for="item in items"
          :key="item.title"
          :to="{name: item.name}"
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-content class='blue-grey lighten-3'>
      <v-btn flat icon color="black" v-if='!mini' @click='mini = true'>
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      <v-btn flat icon color="black" v-else @click='mini = false'>
        <v-icon>keyboard_arrow_right</v-icon>
      </v-btn>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: true,
      items: [
        { title: 'Projects', icon: 'view_agenda', name: 'projects' },
        { title: 'Build SQL query', icon: 'build', name: 'buildsqlquery' },
        { title: 'Pix2Code', icon: 'settings', name: 'pix2code' },
        { title: 'GUI generator', icon: 'show_chart', name: 'guigenerator' },
        { title: 'Statistics', icon: 'insert_chart', name: 'statistics' }
      ],
      mini: true
    }
  }
}
</script>

<style lang="css">
</style>
