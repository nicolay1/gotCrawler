import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from "bootstrap-vue"
import Notifications from 'vue-notification'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAngleDown} from '@fortawesome/free-solid-svg-icons'
import {faHeart} from '@fortawesome/free-solid-svg-icons/faHeart'
import {faHeart as faHeartRegular} from '@fortawesome/free-regular-svg-icons/faHeart'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import App from './App.vue'
import Routes from './routes.js'



library.add(faAngleDown)
library.add(faHeart)
library.add(faHeartRegular)

Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.use(BootstrapVue)
Vue.use(Notifications)
Vue.use(VueRouter);

const router = new VueRouter({
    routes: Routes,
    mode: 'history'
})
new Vue({
    el: '#app',
    components: {App},
    render: h => h(App),
    router: router
});
