import Show from './components/Show.vue'
import ShowVue from './views/ShowVue.vue'
import LandingPage from './views/LandingPage.vue'
import Signup from './components/Signup.vue'
import Login from './components/Login.vue'


export default [
    {path: '/', component: LandingPage},
    {path: '/show/:id', component: Show},
    {path: '/login', component: Login},
    {path: '/signup', component: Signup}
]