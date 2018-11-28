<template lang="html">
  <div>
    <div class="headline">
      {{path[0]}}
    </div>
    <v-flex xs12>
      <v-btn color='red lighten-2' dark :loading='isLoading' @click='showIsortDiff()'>
        Show isort diff
      </v-btn>
      <v-btn color='blue darken-4' dark :loading='isLoading' @click='fixIsortFix()'>
        Fix isort diff
      </v-btn>
    </v-flex>
    <v-layout row class='mt-4 px-2'>
      <v-text-field
        v-model='mcCabeComplexity'
        label="Min McCabe complexity"
        :disabled='isLoading'
        box />
      <v-btn color='blue' dark large :loading='isLoading' @click='displayMcCabe()'>
        McCabe
      </v-btn>
    </v-layout>

    <v-alert :value="successfullImportsFix" type="success">
      Successfully fixed imports ordering
    </v-alert>
    <code v-if='diff' class='language-py pa-3 subheading font-weight-black'>
      <span v-for='(diffLine,index) in diff' :key='index'>{{diffLine}}</span>
    </code>

    <v-data-table
      v-if='mcCabeTableItems.length'
      :headers="headers"
      :items="mcCabeTableItems"
      class="elevation-1"
      hide-actions
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.lineNum }}</td>
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.complexity }}</td>
      </template>
    </v-data-table>

  </div>
</template>

<script>
import {pyIsortDiff, pyIsortFix, pyMcCabe} from '@/api/codeAnalysis'

export default {
  props: ['path'],
  data () {
    return {
      isLoading: false,
      successfullImportsFix: false,
      diff: null,
      mcCabeComplexity: 1,
      mcCabeOutput: [],
      headers: [
        {text: 'Line number'},
        {text: 'Name'},
        {text: 'Complexity'}
      ]
    }
  },
  computed: {
    mcCabeTableItems () {
      let data = []
      for (let item of this.mcCabeOutput) {
        const elements = item.split(' ')
        data.push({
          lineNum: elements[0],
          name: elements[1],
          complexity: elements[2]
        })
      }
      return data
    }
  },
  methods: {
    showIsortDiff () {
      if (this.path.length) {
        this.isLoading = true
        pyIsortDiff(this.path[0]).then(resp => {
          this.diff = resp.data.lines
        }).finally(() => {this.isLoading = false})
      }
    },
    fixIsortFix () {
      if (this.path.length) {
        this.isLoading = true
        pyIsortFix(this.path[0]).then(resp => {
          this.successfullImportsFix = true
        }).finally(() => {this.isLoading = false})
      }
    },
    displayMcCabe () {
      if (this.path.length) {
        this.isLoading = true
        pyMcCabe(this.path[0], this.mcCabeComplexity).then(resp => {
          this.mcCabeOutput = resp.data.lines
        }).finally(() => {this.isLoading = false})
      }
    }
  },
  watch: {
    path () {
      this.diff = null
      this.successfullImportsFix = false
    }
  }
}
</script>

<style lang="css">
</style>
