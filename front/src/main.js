import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import Notifications from 'vue-notification'

import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAngleDown} from '@fortawesome/free-solid-svg-icons'
import {faHeart} from '@fortawesome/free-solid-svg-icons/faHeart'
import {faHeart as faHeartRegular} from '@fortawesome/free-regular-svg-icons/faHeart'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'



library.add(faAngleDown)
library.add(faHeart)
library.add(faHeartRegular)

Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.use(BootstrapVue)
Vue.use(Notifications)

new Vue({
    el: '#app',
    components: {App},
    render: h => h(App)
})
