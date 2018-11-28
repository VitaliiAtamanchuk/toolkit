import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import PathInput from '@/components/PathInput'
import splitPane from 'vue-splitpane'

Vue.config.productionTip = false
Vue.component('PathInput', PathInput);
Vue.component('split-pane', splitPane);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
