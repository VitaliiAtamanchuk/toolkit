<template lang="html">
<div>
  <v-layout align-center justify-center class='py-5 white' v-if='isTreeLoading'>
    <v-progress-circular
      :size="100"
      color="primary"
      indeterminate
    >Loading</v-progress-circular>
  </v-layout>
  <v-treeview
    v-else
    v-model="tree"
    dark
    class='grey darken-3 label-big py-4 px-3'
    :active.sync="activeLocal"
    :open.sync="open"
    :items="items"
    activatable
    item-key="abs_path"
    open-on-click
    hoverable
    transition
    active-class='v-treeview-node--active font-weight-bold indigo--text text--lighten-4'
    selected-color="indigo"
    expand-icon="mdi-chevron-down"
    on-icon="mdi-bookmark"
    off-icon="mdi-bookmark-outline"
  >
    <template slot="prepend" slot-scope="{ item, open, leaf }">
      <v-icon v-if="!item.file">
        {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
      </v-icon>
      <v-icon v-else>
        {{ files[item.file] }}
      </v-icon>
    </template>
    <template slot='append' slot-scope="{ item, open, leaf }">
      <span class='body-2 font-italic grey--text' v-if='item.todos_num'>
        TODOs: {{item.todos_num}}
      </span>
    </template>
  </v-treeview>
</div>
</template>

<script>
export default {
  props: {
    isTreeLoading: {type: Boolean, required: true},
    items: {type: Array, required: true},
    active: {type: Array, required: true}
  },
  data: () => ({
    open: ['src'],
    activeLocal: [],
    files: {
      html: 'mdi-language-html5',
      jinja: 'mdi-language-html5',
      js: 'mdi-nodejs',
      json: 'mdi-json',
      md: 'mdi-markdown',
      pdf: 'mdi-file-pdf',
      png: 'mdi-file-image',
      txt: 'mdi-file-document-outline',
      xls: 'mdi-file-excel',
      sh: 'mdi-console',
      py: 'mdi-language-python',
      pyc: 'mdi-language-python-text',
      vue: 'mdi-vuejs',
      log: 'mdi-history',
      ico: 'mdi-file-image',
      svg: 'mdi-file-image',
      jpg: 'mdi-file-image',
      csv: 'mdi-file-delimited',
      css: 'mdi-language-css3',
      scss: 'mdi-sass'
    },
    tree: []
  }),
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
  },
  watch: {
    activeLocal () {
      this.$emit('update:active', this.activeLocal)
    }
  }
}
</script>

<style lang='scss'>
.label-big * {
  font-size: 1.3rem;
}
.v-treeview-node__content{
  & i.mdi-folder, {
    color: #FFCC80;
  }
  & i.mdi-folder-open {
    color: #FFA726;
  }
  & i.mdi-language-python {
    color: #7986CB;
  }
  & i.mdi-vuejs {
    color: #689F38;
  }
  & i.mdi-nodejs {
    color: #EEFF41;
  }
  & i.mdi-sass {
    color: #F06292;
  }
}
</style>
