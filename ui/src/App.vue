<template>
  <v-app :dark='dark'>
    <v-toolbar dark app color='primary lighten-2'>
      <v-toolbar-title class="headline">
        <router-link class='white--text' :to="{name: 'home'}">Home Dashboard</router-link>
        <!-- <span class="font-weight-light">HomeDashboard</span> -->
      </v-toolbar-title>
    </v-toolbar>

    <v-content>
      <router-view/>
    </v-content>
    <v-footer color='grey darken-1'>
      <v-spacer />
      <v-btn icon @click='dark = !dark'>
        <v-icon>style</v-icon>
      </v-btn>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      dark: false,
    }
  }
}
</script>
