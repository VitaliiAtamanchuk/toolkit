<template lang="html">
  <v-layout row wrap>
    <v-flex xs5 md3 class='mr-3'>
      <v-card :to="{name: 'projects'}" class='pa-3'>
        <v-responsive>
          <v-layout justify-center>
            <v-avatar color="indigo">
              <v-icon dark>book</v-icon>
            </v-avatar>
          </v-layout>
        </v-responsive>
        <v-card-title class='text-xs-center'>
          <v-layout justify-center>
            <span class='body-2 font-weight-medium'>Check Props</span>
          </v-layout>
        </v-card-title>
          <v-divider />
        <v-card-text>
          <v-layout justify-center>
            <ul class='subheading'>
              <li class='my-3'>Prop definitions should be as detailed as possible.</li>
              <li>Prop names should always use camelCase during declaration(in script), but kebab-case in templates and JSX.</li>
            </ul>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: ['id'],
  data () {
    return {
      routes: [
        {
          to: {name: 'projects'},
          desc: [
            {text: 'Prop definitions should be as detailed as possible.', link: 'https://vuejs.org/v2/style-guide/#Prop-definitions-essential'},
            {text: 'Prop names should always use camelCase during declaration(in script), but kebab-case in templates and JSX.', link: 'https://vuejs.org/v2/style-guide/#Prop-name-casing-strongly-recommended'}
          ]
        }
      ]
    }
  }
}
</script>

<style lang="css">
</style>
