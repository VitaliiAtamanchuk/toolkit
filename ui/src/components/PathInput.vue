<template>
  <v-card tile class='elevation-1 pa-3'>
    <v-subheader>
      <span class='title'>Path:</span>
      <span class='font-italic ml-3'>{{prettyPath}}</span>
    </v-subheader>
    <v-combobox
      solo
      multiple
      small-chips
      v-model="path"
      :items="dirs" >
      <template
        slot="selection"
        slot-scope="{ item, parent, selected }">
        <v-chip
          :color="`blue lighten-3`"
          :selected="selected"
          label
          small
        >
          <span>
            /{{ item }}
          </span>
        </v-chip>
      </template>
    </v-combobox>
  </v-card>
</template>

<script>
import _ from 'lodash'

export default {
  data () {
    return {
      path: [],
      dirs: ['home', 'vitalii', 'src', 'POLECMNIE']
    }
  },
  computed: {
    prettyPath() {
      if (this.path.length) {
        return '/' + _.join(this.path, '/') + '/'
      } else {
        return '/'
      }
    }
  }
}  
</script>