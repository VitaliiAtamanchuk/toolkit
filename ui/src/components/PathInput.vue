<template>
  <v-card tile class='elevation-1 pa-3'>
    <v-subheader>
      <span class='title'>Path:</span>
      <span class='font-italic ml-3'>{{prettyPath}}</span>
    </v-subheader>
    <v-layout row>
      <v-flex xs2>
        <v-autocomplete
          v-if='isWindows'
          solo
          v-model="drive"
          :items="drives"
        />
      </v-flex>
      <v-flex xs10>
        <v-combobox
          solo
          multiple
          small-chips
          v-model="pathLocal"
          @input='changeHandler'
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
                {{pathDelimiter}}{{ item }}
              </span>
            </v-chip>
          </template>
        </v-combobox>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
import _ from 'lodash'
import {pathExplore} from '@/api/path'

export default {
  props: ['path'],
  data () {
    return {
      drive: 'C:',
      drives: new Array( 26 ).fill( 1 ).map( ( v, i ) => String.fromCharCode( 65 + i )+":" ),
      pathLocal: [],
      pathDelimiter: window.navigator.platform.startsWith('Win') ? '\\' : '/',
      dirs: []
    }
  },
  computed: {
    prettyPath () {
      let retVal = window.navigator.platform.startsWith('Win') ? this.drive : ''
      if (this.pathLocal.length) {
        retVal += this.pathDelimiter + _.join(this.pathLocal, this.pathDelimiter)
      } else {
        retVal += this.pathDelimiter
      }
      return retVal
    },
    isWindows: () => window.navigator.platform.startsWith('Win')
  },
  watch: {
    drive () {
      const path = this.prettyPath
      pathExplore(path).then(resp => {
        this.dirs = resp.data.dirs
      })
      this.$emit('update:path', path)
    },
    pathLocal:{
      handler () {
        const path = this.prettyPath
        pathExplore(path).then(resp => {
          this.dirs = resp.data.dirs
        })
        this.$emit('update:path', path)
      },
      immediate: true
    }
  },
  methods: {
    changeHandler (val) {
      const selectedValue = val[val.length - 1]
      let mostFamiliarDir = ''
      for (let dir of this.dirs) {
        if (dir.startsWith(selectedValue)) {
          mostFamiliarDir = dir
        }
      }
      this.pathLocal[this.pathLocal.length - 1] = mostFamiliarDir
    }
  }
}
</script>