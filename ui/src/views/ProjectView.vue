<template>
  <div>
    <v-navigation-drawer clipped app permanent floating width='450' class='grey'>
      <v-list two-line class='mx-4'>
        <v-btn color='accent' block class='my-3' :to="{name: 'projectGitStats'}">
          Git stats
          <v-icon right>open_in_new</v-icon>
        </v-btn>
        <v-btn color='accent darken-1' block class='my-3'>
          Manage
          <v-icon right>pan_tool</v-icon>
        </v-btn>
        <v-btn color='accent lighten-1' block class='my-3' :to="{name: 'projectTodos'}">
          Show All TODOS
          <v-icon right>list</v-icon>
        </v-btn>
      </v-list>
      
      <v-divider/>
      <v-treeview
        v-model="tree"
        class='green lighten-3 label-big py-4 px-3'
        :active.sync="active"
        :open.sync="open"
        :items="items"
        activatable
        item-key="abs_path"
        open-on-click
        hoverable
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
          <span class='title font-italic grey--text' v-if='item.todos_num'>
            TODOs: {{item.todos_num}}
          </span>
        </template>
      </v-treeview>
    </v-navigation-drawer>
    <v-flex xs12>
      <v-card-text>
        <div class="title font-weight-medium grey--text pa-3 text-xs-center">
          <router-view/>
        </div>
      </v-card-text>
    </v-flex>
  </div>
</template>

<script>
// TODO: sort items, - folder first, files last
// TODO: reset opened folders
// TODO: consider that design https://github.com/ndamjan/vuetify-treeview-example
// TODO: expansion section with list for links at navigation drawer
import {projectGetTree} from '@/api/project'

export default {
  props: {
    id: {
      required: true,
    }
  },
  data: () => ({
    open: ['src'],
    active: [],
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
      scss: 'mdi-language-css3'
    },
    tree: [],
    items: []
  }),
  created () {
    this.getProjectTree()
  },
  methods: {
    getProjectTree () {
      projectGetTree(this.id).then(resp => {
        this.items = resp.data.tree
      })
    }
  }
}
</script>

<style>
.label-big * {
  font-size: 2rem;
}
</style>
