import Show from './components/Show.vue'
import LandingPage from './views/LandingPage.vue'


export default [
    {path: '/', component: LandingPage},
    {path: '/show/:id', component: Show},
    {path: '/login', component: Show},
    {path: '/signup', component: Show},


]