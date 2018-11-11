<template>
    <b-navbar toggleable="sm" type="dark" variant="dark" top>
        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-navbar-brand class="logo" v-on:click="backToRoot">My Show Notifier</b-navbar-brand>
        <b-collapse is-nav id="nav_collapse">
            <b-navbar-nav class="ml-auto">
                <list-notifications v-if="user.connected()" :id_user="user.id"></list-notifications>
                <b-nav-item v-if="!user.connected()" right v-on:click="connectUser">Connexion</b-nav-item>
                <b-nav-item v-if="user.connected()" right v-on:click="disconnectUser">Déconnexion</b-nav-item>
                <b-nav-item v-if="!user.connected()" right v-on:click="disconnectUser">Inscription</b-nav-item>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
    import ListNotifications from "./ListNotifications.vue";
    import User from '../helpers/user';

    export default {
        name: "NavBar",
        components: {ListNotifications},
        props:{
        },
        data(){
            return {
                user: new User()
            }
        },
        methods:{
            disconnectUser(){
                console.log('disconnect');
                User.disconnect();
                this.$router.go()
            },
            connectUser(){
                this.$router.push('/login');
            },
            backToRoot(){
                this.$router.push('/');
            }
        },
        mounted(){
            console.log("user id:", this.user.id)
        }
    }
</script>
<style scoped>
    .logo{
        cursor: pointer;
    }
</style>