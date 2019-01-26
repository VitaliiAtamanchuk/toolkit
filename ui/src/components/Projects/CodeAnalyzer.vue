<template lang="html">
  <div>
    <v-layout row wrap class="white mb-4" style='height: auto'>
      <v-flex xs12 sm5 class='ma-4'>
        <v-card class='pa-4 elevation-10'>
          <v-btn color='indigo' dark  block large @click='showHierarchy'>
            Show hierarchy
          </v-btn>
          <v-card-title primary-title>
            <div>
              <div>Displays tree chart of component usage</div>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs12 sm5 class='ma-4'>
        <v-card class='pa-4 elevation-10'>
          <v-btn color='indigo' dark large block>
            Lint
          </v-btn>
          <v-card-title primary-title>
            <div>
              <div>Check for style guide</div>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
      <vo-basic v-if='treeData' :data="treeData" :pan="true" :zoom="true" direction='l2r' />
    </v-layout>
  </div>
</template>

<script>
import 'vue-orgchart/dist/style.min.css'
import {getVueFileHierarchy} from '@/api/codeAnalysis'
import { VoBasic } from 'vue-orgchart'

export default {
  props: {
    projectId: {type: Number, required: true},
    active: {type: Array, required: true}
  },
  components: {VoBasic},
  data () {
    return {
      treeData: null
    }
  },
  methods: {
    showHierarchy () {
      if (!this.active.length) {return}
      let path = this.active[0]

      getVueFileHierarchy(this.projectId, this.active[0]).then(resp => {
        console.log(this.active[0])
        console.log(resp.data)
        this.treeData = {
          name: path.replace(/^.*[\\\/]/, '').split('.')[0],
          children: resp.data.tags
        }
      })
    }
  },
  computed: {
    isPyFile () {
      return this.active.length ? this.active[0].split('.').pop() === 'py' : false
    },
    isVueFile () {
      return this.active.length ? this.active[0].split('.').pop() === 'vue' : false
    },
    isJsFile () {
      return this.active.length ? this.active[0].split('.').pop() === 'js' : false
    }
  }
}
</script>

<style lang="css">
</style>
