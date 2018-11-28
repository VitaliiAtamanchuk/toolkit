<template lang="html">
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-btn slot="activator" color='primary' large round>
      Add a project
      <v-icon right dark>add</v-icon>
    </v-btn>
    <v-card>

      <v-card-title>
        <span class="headline">Add a project</span>
      </v-card-title>

      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex xs12>
              <PathInput :path.sync='path' />
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click.native="closeDialog()">Close</v-btn>
        <v-btn dark color="blue darken-1" @click.native="submit()">Submit</v-btn>
      </v-card-actions>

    </v-card>
  </v-dialog>
</template>

<script>
import {projectCreate} from '@/api/project'

export default {
  data () {
    return {
      path: '',
      dialog: false
    }
  },
  methods: {
    closeDialog () {
      this.dialog = false
    },
    submit () {
      projectCreate(this.path)
      this.dialog = false
    }
  }
}
</script>

<style lang="css">
</style>
