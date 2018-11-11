import * as axios from 'axios'

import config from '../../config'
import {push_notif_err, push_notif_err_message} from './notifs'
import Jwt from './jwt'

class ApiHelper {
    constructor() {
        this.__backUrl = config.backUrl;
        this.__jwt = new Jwt()
    }

    checkAuth(){
        if(!this.__jwt.exist()){
            push_notif_err("Vous devez vous authentifier pour acceder à cette ressource.");
            return false
        }else{
            return true
        }
    }

    get(resourcePath, params, enforceAuth=false){
        if(!enforceAuth || enforceAuth===this.checkAuth())
            return new Promise(
                (resolve,reject) => axios.get(
                    this.__backUrl + resourcePath, {
                        params,
                        headers: {
                            Authorization: this.__jwt.bearerToken()
                        }
                    }
                 )
                .then((res) => resolve(res.data))
                .catch((err) => push_notif_err(err))
            );
        else
            push_notif_err_message("You should be connected to access this ressource")
    }
    post(resourcePath, params, enforceAuth=false) {
        if (!enforceAuth || enforceAuth === this.checkAuth()) {
            return new Promise(
                (resolve, reject) => axios.post(
                    this.__backUrl + resourcePath, params, {
                        headers: {
                            Authorization: this.__jwt.bearerToken()
                        }
                    }
                )
                    .then((res) => resolve(res.data))
                    .catch((err) => push_notif_err(err))
            );
        }else {
            push_notif_err_message("You should be connected to access this ressource")
        }

    }
    put(ressourcePath, params, enforceAuth=false) {
        if(!enforceAuth || enforceAuth===this.checkAuth())
            return new Promise(
                (resolve, reject) => axios.put(
                    this.__backUrl + ressourcePath,
                    params,
                    {
                        headers: {
                            Authorization: this.__jwt.bearerToken()
                        }
                    }
                )
                .then((res) => resolve(res.data))
                .catch((err) => push_notif_err(err))
            );
        else
            push_notif_err_message("You should be connected to access this ressource")
    }
    delete(resourcePath, enforceAuth=false){
        if(!enforceAuth || enforceAuth===this.checkAuth())
            return new Promise(
                (resolve,reject) => axios.delete(
                    this.__backUrl + resourcePath, {
                        headers: {
                            Authorization: this.__jwt.bearerToken()
                        }
                    }
                )
                .then((res) => resolve(res.data))
                .catch((err) => push_notif_err(err))
        );
        else
            push_notif_err_message("You should be connected to access this ressource")
    }
}

export default new ApiHelper()