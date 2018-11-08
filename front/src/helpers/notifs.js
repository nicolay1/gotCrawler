import Vue from 'vue';

export const push_notif_success = (message) =>{
    Vue.nextTick(() => Vue.notify({
        type: 'success',
        title: 'Erreur',
        text: message
    }))
}

export const push_notif_err = (error) => {
    let message = "Erreur interne sur le serveur."
    if (error.response) {
        message = error.response.data
    }
    Vue.nextTick(() => {Vue.notify({
        type: 'error',
        title: 'Erreur',
        text: message
    })})
}