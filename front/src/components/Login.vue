<template>
    <b-card class="bg-light">
    <b-form @submit="onSubmit">
      <b-form-group id="loginInputGroup"
                    label="Votre login:"
                    label-for="loginInput">
        <b-form-input id="loginInputGroup"
                      type="text"
                      v-model="form.login"
                      required
                      placeholder="Entrez votre login">
        </b-form-input>
      </b-form-group>
      <b-form-group id="pwdInputGp"
                    label="Votre mot de passe:"
                    label-for="pwdInput">
        <b-form-input id="pwdInput"
                      type="password"
                      required
                      v-model="form.pwd"
                      placeholder="Entrez votre mot de passe">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Connexion</b-button>
    </b-form>
  </b-card>
</template>

<script>
  import apiHelper from '../helpers/api.js';
  import {push_notif_success} from '../helpers/notifs.js'

  export default {
        name: 'Login',
        data(){
            return {
                    form: {
                        login: "",
                        pwd: "",
                    }
            }
        },
        methods: {
            onSubmit (evt) {
                evt.preventDefault();

                apiHelper.post('auth', this.form, true)
                    .then(
                        (res) => this.$router.push("/")
                    )
            }
        }

  }
</script>