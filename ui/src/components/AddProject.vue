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
              <PathInput />
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click.native="closeDialog()">Close</v-btn>
        <v-btn dark color="blue darken-1" @click.native="closeDialog()">Submit</v-btn>
      </v-card-actions>

    </v-card>
  </v-dialog>
</template>

<script>
import PathInput from '@/components/PathInput'

export default {
  components: {PathInput},
  data () {
    return {
      dialog: false,
      projectPath: '',
      search: null,
      dirs: ['home', 'vitalii', 'src', 'POLECMNIE']
    }
  },
  methods: {
    closeDialog () {
      this.dialog = false
    }
  }
}
</script>

<style lang="css">
</style>
