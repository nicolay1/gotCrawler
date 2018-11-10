<template>
    <b-navbar type="dark" variant="dark" top>
        <b-navbar-brand router-link-to="/">NomDuProduit</b-navbar-brand>
                <b-nav-item right router-link-to="/signout">Déconnexion
                </b-nav-item>
    </b-navbar>
</template>

<script>
    export default {
        name: "NavBar",
        props:{
        }
    }
</script>

<style scoped>

</style>