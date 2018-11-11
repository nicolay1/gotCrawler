<template>
    <b-container>
        <b-card>
            <b-row>
                <b-col cols="3">
                    <b-img top :src="user.poster" width="250" height="250"></b-img>
                </b-col>
                <b-col cols="9">
                    <div class="name">Prénom: {{user.firstname}}</div>
                    <div class="name">Nom: {{user.surname}}</div>

                </b-col>
            </b-row>
        </b-card>
    </b-container>
</template>

<script>
    import User from '../helpers/user.js';

    export default {
        name: "User",
        data() {
            return {
                user: new User(),
            }
        },
        created() {
            if (!this.user.connected()) {
                this.$router.push('/');
                this.$notify({
                    type: 'error',
                    title: 'Erreur',
                    text: "Vous n'êtes pas connectés"

                })
            }
        }
    }
</script>

<style scoped>
    .name {
        text-align: center;
        margin-top: 20px;
        font-size: large;
        font-weight: bold;
    }
</style>