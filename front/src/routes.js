import Show from './components/Show.vue'
import ShowVue from './views/ShowVue.vue'
import LandingPage from './views/LandingPage.vue'


export default [
    {path: '/', component: LandingPage},
    {path: '/show/:id', component: ShowVue},
    {path: '/login', component: Show},
    {path: '/signup', component: Show},


]