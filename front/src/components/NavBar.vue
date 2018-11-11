<template>
    <b-navbar toggleable="md" type="dark" variant="dark" top>
          <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-navbar-brand router-link-to="/">NomDuProduit</b-navbar-brand>
        <b-collapse is-nav id="nav_collapse">
            <b-navbar-nav class="ml-auto">
                <list-notifications></list-notifications>
            </b-navbar-nav>
        </b-collapse>

        <b-nav-item router-link-to="/signout" right>Déconnexion
        </b-nav-item>
    </b-navbar>
</template>

<script>
    import ListNotifications from "./ListNotifications.vue";

    export default {
        name: "NavBar",
        components: {ListNotifications},
        props: {}
    }
</script>

<style scoped>

</style>