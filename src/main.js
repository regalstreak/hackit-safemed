import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import VueQrcodeReader from 'vue-qrcode-reader'

import VueParticles from 'vue-particles'
Vue.use(VueParticles)

Vue.config.productionTip = false


Vue.use(VueQrcodeReader)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
