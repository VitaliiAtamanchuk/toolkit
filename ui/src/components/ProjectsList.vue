<template lang="html">
  <v-layout row wrap>
      <span class="display-2 text-uppercase font-weight-medium">Projects</span>
      <v-spacer/>
      <AddProject />
    <v-flex xs12 class='my-3'>
      <v-divider style='border-width: 1.6px 0 0;' />
    </v-flex>
    <v-flex xs12>
      <v-list two-line subheader>

        <v-list-tile avatar @click="">
          <v-list-tile-avatar>
            <v-icon class="primary lighten-2 grey lighten-1 white--text">folder</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>POLECMNIE</v-list-tile-title>
            <v-list-tile-sub-title>Jan 9, 2014</v-list-tile-sub-title>
          </v-list-tile-content>

          <v-list-tile-action>
            <v-layout row>
              <v-btn icon ripple class='mr-4'>
                <v-icon color="grey lighten-1">open_in_browser</v-icon>
              </v-btn>
              <v-btn icon ripple class='mr-3'>
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
import AddProject from '@/components/AddProject'

export default {
  components:{AddProject}
}
</script>

<style lang="css">
</style>
