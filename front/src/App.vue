<template>
    <div id="app">
        <nav-bar></nav-bar>
        <notifications 
                    position="top right"
                    :speed="500"
                    :duration="10000"/>
        <router-view>

        </router-view>

        <footer-nav></footer-nav>
    </div>
</template>

<script>

    import NavBar from "./components/NavBar.vue";
    import FooterNav from "./components/FooterNav.vue";
    export default {
        name: 'App',
        components: {FooterNav, NavBar},
    }
</script>

<style>
    #app {

    }
</style>