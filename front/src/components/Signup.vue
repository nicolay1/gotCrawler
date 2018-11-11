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
      <b-form-group id="firstnameInputGroup"
                    label="Votre prénom et votre nom:"
                    label-for="firstnameInput">
        <b-form-input id="firstnameInput"
                      type="text"
                      v-model="form.firstname"
                      required
                      placeholder="Entrez votre prénom">
        </b-form-input>
      </b-form-group>
      <b-form-group id="surnameInputGroup"
                    label="Votre nom:"
                    label-for="surnameInput">
        <b-form-input id="surnameInput"
                      type="text"
                      required
                      v-model="form.surname"
                      placeholder="Entrez votre nom">
        </b-form-input>
      </b-form-group>
      <b-form-group id="posterInputGroup"
                    label="Url de la photo de profil:"
                    label-for="posterInput">
        <b-form-input id="posterInput"
                      type="text"
                      required
                      v-model="form.poster"
                      placeholder="Entrez l'url de votre photo de profil">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Inscription</b-button>
    </b-form>
  </b-card>
</template>

<script>
  import apiHelper from '../helpers/api.js';
  import {push_notif_success} from '../helpers/notifs.js'

  export default {
        name: 'Inscription',
        data(){
            return {
                    form: {
                        login: "",
                        firstname: "",
                        surname: "",
                        pwd: "",
                        poster: ""
                    }
            }
        },
        methods: {
            onSubmit (evt) {
                evt.preventDefault();
                apiHelper.post('user', this.form, true)
                    .then(
                        (jwtToken) => {
                            push_notif_success("Votre inscription a bien été prise en compte, bienvenue !")
                            window.localStorage.setItem("jwtToken", jwtToken)
                        }
                    )
            }
        }
  }
</script>