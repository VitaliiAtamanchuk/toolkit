<template>
  <v-app :dark='dark'>
    <v-toolbar dark app color='primary lighten-2'>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>open_in_new</v-icon>
      </v-btn>
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
