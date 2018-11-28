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
        <v-btn color='accent lighten-1' block class='my-3' :to="{name: 'projectAnalyzeVue'}">
          Analyze Vue Code
          <v-icon right>list</v-icon>
        </v-btn>
      </v-list>

      <v-divider/>
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
        :active.sync="active"
        :open.sync="open"
        :items="items"
        activatable
        item-key="abs_path"
        open-on-click
        hoverable
        transition
        active-class='v-treeview-node--active font-weight-bold light-blue--text'
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
          <span class='title font-italic grey--text' v-if='item.todos_num'>
            TODOs: {{item.todos_num}}
          </span>
        </template>
      </v-treeview>
    </v-navigation-drawer>

    <split-pane :min-percent='20' :default-percent='70' split="vertical">
      <template slot="paneL">
        <div class="white mt-0 pt-2 pl-2" style='min-height: 100vh;'>
          <v-expansion-panel class='mb-4 elevation-10'
            v-if='active.length' v-model='todosExpandPanel'>
            <v-expansion-panel-content>
              <div slot="header">File TODOs</div>
              <v-divider/>
              <v-card class='pa-4'>
                <v-list class='elevation-3' three-line>
                  <template v-for="(item, index) in activeFileTodos">
                    <v-list-tile>
                      <v-list-tile-content>
                        <v-list-tile-title class='title'>
                          {{item.line_num}}: -
                          {{item.text}}
                        </v-list-tile-title>
                        <v-list-tile-sub-title class="subheading my-1">
                          {{getAuthor(item.author)}}
                        </v-list-tile-sub-title>
                        <v-list-tile-sub-title>
                          {{ item.date }}
                        </v-list-tile-sub-title>
                      </v-list-tile-content>
                    </v-list-tile>
                    <v-divider/>
                  </template>
                </v-list>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <ThePyFileAnalysis :path='active' v-if='isPyFile' />
          <TheVueFileAnalysis :path='active' v-else-if='isVueFile' />
          <div v-else class='display-1 ma-5'> Select a file</div>
        </div>
      </template>
      <template slot="paneR">
        <div class="white">
          <router-view/>
        </div>
      </template>
    </split-pane>

  </div>
</template>

<script>
// TODO: sort items, - folder first, files last
// TODO: reset opened folders
// TODO: consider that design https://github.com/ndamjan/vuetify-treeview-example
// TODO: expansion section with list for links at navigation drawer
import {projectGetTree} from '@/api/project'
import {getFileTodos} from '@/api/codeAnalysis'
import ThePyFileAnalysis from '@/components/ThePyFileAnalysis'
import TheVueFileAnalysis from '@/components/TheVueFileAnalysis'

export default {
  components: {ThePyFileAnalysis, TheVueFileAnalysis},
  props: {
    id: {
      required: true,
    }
  },
  data: () => ({
    todosExpandPanel: 0,
    isTreeLoading: false,
    diff: [],
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
      scss: 'mdi-sass'
    },
    tree: [],
    activeFileTodos: [],
    activeFileTodosNum: 0,
    items: []
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
  created () {
    this.getProjectTree()
  },
  methods: {
    getProjectTree () {
      this.isTreeLoading = true
      projectGetTree(this.id).then(resp => {
        this.items = resp.data.tree
      }).finally(() => {this.isTreeLoading = false})
    },
    getAuthor (author) {
      if (author) {
        return author
      }
      return 'None'
    }
  },
  watch: {
    active (val) {
      if (val.length) {
        this.todosExpandPanel = 0
        getFileTodos(this.id, val[0]).then(resp => {
          this.activeFileTodos = resp.data.todos
          this.activeFileTodosNum = resp.data.todos_num
        })
      }
    }
  }
}
</script>

<style lang='scss'>
.label-big * {
  font-size: 1.7rem;
}
.splitter-pane-resizer.vertical {
  height: 100vh !important;
  width: 20px !important;
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
